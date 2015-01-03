
import wx
import wx.xrc
from Printer import *


MAX_PIECES =  5

###########################################################################
## Class OrderFrame
###########################################################################

## Fereastra de finalizare a comenzii

class OrderFrame ( wx.Frame ):
	
	def __init__( self, parent, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Finish", 
			pos = wx.DefaultPosition, size = wx.Size( 450,470 ), 
			style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL)
		
		self.options = options
		self.parent = parent


		icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
		icon.CopyFromBitmap(wx.Bitmap("img/finalize_project.png"))
		self.SetIcon(icon)
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )


		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		

		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_window = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.main_window.SetScrollRate( 5, 5 )
		self.main_window.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )
		
		layout_sizer = wx.BoxSizer( wx.VERTICAL )
		
		top_sizer = wx.GridBagSizer( 0, 0 )
		top_sizer.SetFlexibleDirection( wx.BOTH )
		top_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.found_label = wx.StaticText( self.main_window, wx.ID_ANY, u"Fault found:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.found_label.Wrap( -1 )
		top_sizer.Add( self.found_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.found_field = wx.TextCtrl( self.main_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.found_field.SetMinSize( wx.Size( 150,50 ) )
		
		top_sizer.Add( self.found_field, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
		
		services_choiceChoices = []
		self.services_choice = wx.ListBox( self.main_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, services_choiceChoices, 0 )
		self.services_choice.SetMinSize( wx.Size( 150,50 ) )
		
		top_sizer.Add( self.services_choice, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.services_label = wx.StaticText( self.main_window, wx.ID_ANY, u"Service:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.services_label.Wrap( -1 )
		top_sizer.Add( self.services_label, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
		
		self.return_label = wx.StaticText( self.main_window, wx.ID_ANY, u"Returned date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.return_label.Wrap( -1 )
		top_sizer.Add( self.return_label, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.warrant_label = wx.StaticText( self.main_window, wx.ID_ANY, u"Warranty:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.warrant_label.Wrap( -1 )
		top_sizer.Add( self.warrant_label, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.comments_label = wx.StaticText( self.main_window, wx.ID_ANY, u"Comments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.comments_label.Wrap( -1 )
		top_sizer.Add( self.comments_label, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 6 ), wx.ALL, 5 )
		
		self.comments_field = wx.TextCtrl( self.main_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.comments_field.SetMinSize( wx.Size( 150,50 ) )
		self.comments_field.SetMaxLength(100)

		top_sizer.Add( self.comments_field, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.return_date_ctrl = wx.DatePickerCtrl( self.main_window, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		top_sizer.Add( self.return_date_ctrl, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.warrant_ctrl = wx.SpinCtrl( self.main_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 36, 0 )
		self.warrant_ctrl.SetMinSize( wx.Size( 70,-1 ) )
		self.warrant_ctrl.SetMaxSize( wx.Size( 70,-1 ) )
		
		top_sizer.Add( self.warrant_ctrl, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		
		layout_sizer.Add( top_sizer, 0, wx.EXPAND, 5 )
		
		self.static_line = wx.StaticLine( self.main_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		layout_sizer.Add( self.static_line, 0, wx.ALL|wx.EXPAND, 5 )	

		self.pieces_panel = PPanel( self.main_window )

		layout_sizer.Add( self.pieces_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		bottom_sizer = wx.GridBagSizer( 0, 0 )
		bottom_sizer.SetFlexibleDirection( wx.BOTH )
		bottom_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		icon = wx.Bitmap("img/service_out.png")		
		self.print_out_button = wx.BitmapButton( self.main_window, wx.ID_ANY, icon, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		icon = wx.Bitmap("img/warrant_icon.png")		
		self.print_warrant_button = wx.BitmapButton( self.main_window, wx.ID_ANY, icon, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		bottom_sizer.Add(self.print_out_button, wx.GBPosition(0, 2))
		bottom_sizer.Add(self.print_warrant_button, wx.GBPosition(0, 3))

		self.total_price_label = wx.StaticText( self.main_window, wx.ID_ANY, u"Total Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.total_price_label.Wrap( -1 )
		bottom_sizer.Add( self.total_price_label, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.total_price_field = wx.TextCtrl( self.main_window, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bottom_sizer.Add( self.total_price_field, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.ok_button = wx.Button( self.main_window, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bottom_sizer.Add( self.ok_button, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_window, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bottom_sizer.Add( self.cancel_button, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		layout_sizer.Add( bottom_sizer, 0, wx.EXPAND, 5 )
		
		
		self.main_window.SetSizer( layout_sizer )
		self.main_window.Layout()
		layout_sizer.Fit( self.main_window )
		main_sizer.Add( self.main_window, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.OnPrintOut, self.print_out_button)
		self.Bind(wx.EVT_BUTTON, self.OnPrintWarrant, self.print_warrant_button)

		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		

		self.Init()

		self.MakeModal(True)
		self.Show()

		self.parent.PRINTER = Printer(self.parent)


	def OnPrintOut(self, event):
		data = self.parent.database.GetProjectLarge(self.project_id)
		self.parent.PRINTER.Print(data, 'service_eliberare.png', 'service_eliberare')

	def OnPrintWarrant(self, event):
		data = self.parent.database.GetProjectLarge(self.project_id)
		self.parent.PRINTER.Print(data, 'garantie.png', 'garantie_service')



	def __del__( self ):
		pass

	def Init(self):

		self.project_id   = self.options[0]
		
		# initializam tabelul cu servicii
		services = self.parent.database.GetServices()
		self.services_choices = {}
		for service in services[0]:
			self.services_choices[service[1]] = service[0]

		try:
			self.services_choice.SetItems(self.services_choices.keys())
			self.service_id   = self.options[10]
		except:
			print 'Error'


		# selectam serviciul	
		for service in self.services_choices:
			if self.services_choices[service] == self.service_id:
				row = self.services_choice.FindString(service)
				self.services_choice.SetSelection(row)
				break



		self.found_field.SetValue(self.options[5])


		#self.returned     = self.options[7]

		self.pieces_panel.SetData(String_toPP([self.options[11], self.options[12]]))
		try:
			self.warrant_ctrl.SetValue(self.options[13])
		except:
			self.warrant_ctrl.SetValue(0)

		self.comments_field.SetValue(self.options[14])
		self.total_price_field.SetValue(self.options[15])

		try:
			date_obj = wx.DateTime()
			date_obj.ParseFormat(self.options[8], '%Y-%m-%d')
			self.return_date_ctrl.SetValue(date_obj)
		except:
			pass

	
	def OnPressOk(self, event):
		data = PP_toString(self.pieces_panel.GetFullData())
		found        = self.found_field.GetValue()
		returned     = self.return_date_ctrl.GetValue().Format('%Y-%m-%d')

		try:
			service_name = self.services_choice.GetString(self.services_choice.GetSelection())	
			service_id =   self.services_choices[service_name]
		except wx._core.PyAssertionError:
			service_id = None
		
		change_piece = data[0]
		price_piece  = data[1]
		warrant      = self.warrant_ctrl.GetValue()
		comments     = self.comments_field.GetValue()
		total_price  = self.total_price_field.GetValue()
		project = [found, returned, service_id, change_piece, price_piece,
		warrant, comments, total_price]
		None_toEmptyString(project)
		self.parent.database.FinishProject(self.project_id, project)

		self.OnExit(None)
	
	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()











class PItem(wx.Panel):

	def __init__(self, parent, index):
		super(PItem, self).__init__(parent = parent)

		self.index = index

		piece_field_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		delete_icon = wx.Bitmap("img/delete_icon_small.png")		
		self.delete_button = wx.BitmapButton( self, wx.ID_ANY, delete_icon, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		piece_field_sizer.Add( self.delete_button, 0, wx.LEFT, 5 )
		
		self.piece_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.piece_field.SetMaxLength( 20 ) 
		self.piece_field.SetMaxSize( wx.Size( 210,-1 ) )
	
		piece_field_sizer.Add( self.piece_field, 3, wx.ALL, 5 )
		
		self.price_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_field.SetMaxLength( 10 ) 
		self.price_field.SetMaxSize( wx.Size( 100,-1 ) )
		
		piece_field_sizer.Add( self.price_field, 0, wx.ALL, 5 )

		self.SetSizer(piece_field_sizer)

		self.Bind(wx.EVT_BUTTON, self.OnDelete, self.delete_button)

	def OnDelete(self, event):
		self.Hide()
		self.GetParent().DeleteRow(self)

	def SetPiece(self, piece):
		self.piece_field.SetValue(piece)

	def GetPiece(self):
		return self.piece_field.GetValue()

	def SetPrice(self, price):
		self.price_field.SetValue(price)

	def GetPrice(self):
		return self.price_field.GetValue()



class PPanel(wx.Panel):

	def __init__(self, parent):
		super(PPanel, self).__init__(parent = parent)

		self.parent = parent
		self.rows = 0
		
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )
		
		self.pieces_sizer = wx.BoxSizer( wx.VERTICAL )
		
		pieces_label_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		add_icon = wx.Bitmap("img/add_piece_row.png")
		self.add_button = wx.BitmapButton( self, wx.ID_ANY, add_icon, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		pieces_label_sizer.Add( self.add_button, 0, wx.ALL, 5 )
		
		self.piece_change_label = wx.StaticText( self, wx.ID_ANY, u"Changed piece", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.piece_change_label.Wrap( -1 )
		pieces_label_sizer.Add( self.piece_change_label, 3, wx.ALL, 10 )
		
		self.price_label = wx.StaticText( self, wx.ID_ANY, u"            Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_label.Wrap( -1 )
		self.price_label.SetMaxSize( wx.Size( 200,-1 ) )
		
		pieces_label_sizer.Add( self.price_label, 2, wx.ALL, 10 )
		self.pieces_sizer.Add( pieces_label_sizer, 0, wx.EXPAND, 5 )
		

		self.pitems_heap = []	# rindurile neutilizare
		self.pitems_show = []   # rindurile utilizate

		for i in range(MAX_PIECES):
			new_item = PItem(self, i)	# cream rinduri si le punem in heap (neutilizate)
			self.pieces_sizer.Add(new_item, 0, wx.EXPAND, 5)
			self.pitems_heap.append(new_item)
			new_item.Hide()

		self.SetSizer( self.pieces_sizer )
		self.Layout()
		self.pieces_sizer.Fit( self )

		self.OnAddRow(None)	# adaugam un rind


		self.Bind(wx.EVT_BUTTON, self.OnAddRow, self.add_button)

	def OnAddRow(self, event):		# la adaugarea unui rind

		try:
			new_row = self.pitems_heap.pop()	# scoatem din multimea celor neutilizate (daca sunt)
		except:
			return
		new_row.Show()
		self.pitems_show.append(new_row)

		def getkey(item):
			return item.index

		self.pitems_show.sort(None, getkey)

		i = 0
		for row in self.pitems_show:
			if row.index == new_row.index:
				break
			i = i + 1

		while i < len(self.pitems_show) - 1:
			self.pitems_show[i].SetPiece(self.pitems_show[i+1].GetPiece())
			self.pitems_show[i].SetPrice(self.pitems_show[i+1].GetPrice())
			i = i + 1
		self.pitems_show[i].SetPiece('')
		self.pitems_show[i].SetPrice('')

		self.Layout()
		self.parent.Layout()
		self.parent.FitInside()

	def DeleteRow(self, item):

		self.pitems_heap.append(item)
		self.pitems_show.remove(item)
		self.Layout()
		self.parent.Layout()
		self.parent.FitInside()

	def SetData(self, data):	# setam datele pe fiecare rind

		for i in range(len(data) - 1):
			self.OnAddRow(None)

		i = 0
		if len(data) == 0:
			return

		for item in self.pitems_show:
			item.SetPiece(data[i][0])
			item.SetPrice(data[i][1])
			i = i + 1


	def GetFullData(self):
		data = []
		for row in self.pitems_show:
			data.append((row.GetPiece(), row.GetPrice()))

		return data



# Parsers 

def PP_toString(data):

	parsed = ['', '']
	i = 1
	for item in data:
		parsed[0] = parsed[0] + '#' + item[0] 
		parsed[1] = parsed[1] + '#' + item[1] 
		i = i + 1
	return parsed

def String_toPP(data):

	parsed_piece = data[0].split('#')
	parsed_price = data[1].split('#')
	parsed_piece.pop(0)
	parsed_price.pop(0)
	parsed = []
	for i in range(len(parsed_piece)):
		parsed.append([parsed_piece[i], parsed_price[i]])
	return parsed


def None_toEmptyString(data):

	for i in range(len(data)):
		if data[i] == None:
			data[i] = ''

def EmptyString_toNone(data):
	
	for i in range(len(data)):
		if data[i] == '':
			data[i] = None

# if __name__ == '__main__':
# 	app = wx.App(False)
# 	mybitmap = wx.Bitmap("img/delete_icon_small.png")
# 	frame = OrderFrame(None, None)
# 	frame.Show()
# 	app.MainLoop()
