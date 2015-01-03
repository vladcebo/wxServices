import wx
import  wx.lib.mixins.listctrl  as  listmix
import  wx.grid as gridlib


# Clasa lucreaza cu tabelul propriu zis, afisarea elementelor


class CustomDataTable(gridlib.PyGridTableBase):
    def __init__(self):
        gridlib.PyGridTableBase.__init__(self)

        self.colLabels = []
        self.data = []

    def GetNumberRows(self):
        return len(self.data) + 1

    def GetNumberCols(self):
        try:
        	return len(self.data[0])
        except IndexError:
        	return 0


    def IsEmptyCell(self, row, col):
        try:
            return not self.data[row][col]
        except IndexError:
            return True

    def GetValue(self, row, col):
        try:
            return self.data[row][col]
        except IndexError:
            return ''

    def SetValue(self, row, col, value):
        def innerSetValue(row, col, value):
            try:
                self.data[row][col] = value
            except IndexError:
                # add a new row
                self.data.append([''] * self.GetNumberCols())
                innerSetValue(row, col, value)

                # tell the grid we've added a row
                msg = gridlib.GridTableMessage(self,            # The table
                        gridlib.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
                        1                                       # how many
                        )

                self.GetView().ProcessTableMessage(msg)
        innerSetValue(row, col, value) 


    def GetColLabelValue(self, col):
        return self.colLabels[col]


    def CanSetValueAs(self, row, col, typeName):
        return self.CanGetValueAs(row, col, typeName)



class DBTable(gridlib.Grid):

	def __init__(self, parent):
		super(DBTable, self).__init__(parent = parent, style=wx.HSCROLL|wx.VSCROLL)
		self.AdjustScrollbars()

		self.parent = parent
		self.SetCellHighlightPenWidth(0)
		self.table = CustomDataTable()

		self.SetTable(self.table)

		self.SetRowLabelSize(0)
		self.SetMargins(0,0)
		self.AutoSizeColumns(True)
		self.SetDefaultCellOverflow(False)

		
	
	def PutItems(self, data):	
		self.table = CustomDataTable()
		self.table.colLabels = data[1]
		self.table.data = data[0]
		self.SetTable(self.table)
		self.AutoSizeColumns()
		self.ForceRefresh()
 		self.SetSelectionMode(gridlib.Grid.wxGridSelectRows)





class DBList(wx.ListCtrl, listmix.ColumnSorterMixin):

	def __init__(self, parent, size):
		
		super(DBList, self).__init__(parent = parent, 
			style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES 
			| wx.LC_AUTOARRANGE | wx.LC_VIRTUAL | wx.LC_SINGLE_SEL, size = size)


    # data trebuie sa fie o lista din 2 liste unde prima lista contine datele necesare
    # iar a 2-a lista contine coloanele 

	def PutItems(self, data):
		self.ClearAll()
		i = 0
		for col in data[1]:
			self.InsertColumn(i, col)
			i = i + 1
		self.itemDataMap = data[0]
		self.itemIndexMap = range(0, len(data[0]))
		self.SetItemCount(len(data[0]))

	def OnGetItemText(self, item, col):
		index=self.itemIndexMap[item]
		s = self.itemDataMap[index][col]
		return s

