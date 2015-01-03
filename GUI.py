

import wx, time
from   DBTable import *
from   SQLite  import *
from   Order   import *
from   Printer import *
import wx.xrc
import wx.aui
import wx.grid

MAIN_FRAME_WIDTH      = 650
MAIN_FRAME_HEIGHT     = 700
MAIN_FRAME_MIN_WIDTH  = 800
MAIN_FRAME_MIN_HEIGHT = 800
CURRENT_TABLE         = 'Clients'
CURRENT_TABLE_DATA    = None
CURRENT_TABLE_SHOWN   = None
USER_ID               = ""
USER_NAME             = ""

logNULL = wx.LogNull()

columns_dictionary = { 'id'  : 'ID',
'first_name'    : 'First Name',
'last_name'     : 'Last Name',
'name'			: 'Name',
'company_name'  : 'Company',
'ser'           : 'Serial',
'worker'        : 'Engineer',
'pr_name'       : 'Product',
'p_date'        : 'Registered',
'due'           : 'Due Date',
'return'        : 'Returned',
'dname'         : 'Name',
'stock'         : 'Stock',
'price'         : 'Price',
'type'          : 'Type',
'saler'         : 'Saler',
's_date'        : 'Sale Date',
'address'       : 'Address',
'phone'         : 'Phone'}





class LoginFrame ( wx.Dialog ):
	
	def __init__( self, parent, title ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 280, 245 ), style = wx.DEFAULT_DIALOG_STYLE )
		

		self.parent = parent
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.GridBagSizer( 0, 0 )
		main_sizer.SetFlexibleDirection( wx.BOTH )
		main_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		# There may be issues with PNG (RGB iCCP profile error)

		main_logo = wx.Bitmap('img/main_logo.png', wx.BITMAP_TYPE_PNG)


		self.Main_Logo = wx.StaticBitmap( self, wx.ID_ANY, main_logo, wx.DefaultPosition, wx.DefaultSize, 0 )
		main_sizer.Add( self.Main_Logo, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )

		self.login_label = wx.StaticText( self, wx.ID_ANY, u"Login:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login_label.Wrap( -1 )
		main_sizer.Add( self.login_label, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.password_label = wx.StaticText( self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password_label.Wrap( -1 )
		main_sizer.Add( self.password_label, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.login_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login_field.SetMaxLength( 20 ) 
		main_sizer.Add( self.login_field, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL | wx.EXPAND, 5 )
		
		self.password_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		main_sizer.Add( self.password_field, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.ALL | wx.EXPAND, 5 )
		
		self.login_button = wx.Button( self, wx.ID_ANY, u"Log in", wx.DefaultPosition, wx.DefaultSize, 0 )
		main_sizer.Add( self.login_button, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.exit_button = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		main_sizer.Add( self.exit_button, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Bind(wx.EVT_BUTTON, self.OnClose, self.exit_button)
		self.Bind(wx.EVT_BUTTON, self.OnLogin, self.login_button)

		self.SetSizer( main_sizer )
		self.Layout()

		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

	def OnClose(self, event):
		self.EndModal(0)

	def OnLogin(self, event):
		
		global USER_ID, USER_NAME
		database =  Database('databases/it_services.sqlite')
		login = self.login_field.GetValue()
		password =self.password_field.GetValue()
		# don't verify the password
		self.EndModal(1)  # comment this line
		logger = database.CheckLogin(login, password)
		if logger != None:
			USER_ID = logger[0]
			USER_NAME = logger[1]
			self.EndModal(1)
		else:
			pass





###########################################################################
## Class AboutBox
###########################################################################

class AboutBox ( wx.Dialog ):
	
	def __init__( self, parent ):


		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = 'Despre', pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		bitmap = wx.Bitmap("img/main_logo.png")
		

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, bitmap, wx.DefaultPosition, wx.Size( 150,100 ), 0 )
		gbSizer11.Add( self.m_bitmap2, wx.GBPosition( 0, 11 ), wx.GBSpan( 1, 12 ), wx.ALL, 5 )
		

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Feel free to write: cebotari.vladislav@gmail.com", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText55.Wrap( -1 )
		gbSizer11.Add( self.m_staticText55, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 30 ), wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.m_button15, wx.GBPosition( 3, 13 ), wx.GBSpan( 1, 30 ), wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Bind(wx.EVT_BUTTON, self.OnOK, self.m_button15)
	
	def __del__( self ):
		pass

	def OnOK(self, event):
		self.Destroy()
	








class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'UPGRADE', pos = wx.DefaultPosition, 
			size = wx.Size(MAIN_FRAME_WIDTH , MAIN_FRAME_HEIGHT ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.Colour( 242, 245, 255 ) )
		
		self.USER_ID    = USER_ID
		self.USER_NAME  = USER_NAME
		self.PRINTER    = Printer(self)


		icon = wx.Icon('upgrade_icon.ico', wx.BITMAP_TYPE_ICO)

		self.SetIcon(icon)
		try:
			self.SetTitle('UPGRADE - '+ USER_NAME)
		except:
			pass
		mybitmap  = wx.Bitmap("img/images.jpg")	
		mybitmap2 = wx.Bitmap("img/images2.jpg")
		
		main_sizer = wx.BoxSizer(wx.HORIZONTAL)
		
		self.LeftPanel = wx.Panel(self)

		left_sizer = wx.BoxSizer( wx.VERTICAL )
		left_sizer.SetMinSize( wx.Size( 200,-1 ) ) 
		
		################################################################################
		# Toolbarurile pentru alegerea tabelelor pe care le dorim
		################################################################################

		left_TB_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.left_top_toolbar = wx.ToolBar(self.LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.left_top_toolbar.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )


		TB_clients_icon = wx.Bitmap("img/tb_clients.png")

	
		TB_clients = self.left_top_toolbar.AddLabelTool( wx.ID_ANY, u"tool", TB_clients_icon, longHelp = 'Show clients')
		

		TB_products_icon = wx.Bitmap("img/tb_products.png")


		TB_products = self.left_top_toolbar.AddLabelTool( wx.ID_ANY, u"tool",TB_products_icon)

		
		TB_services_icon = wx.Bitmap("img/tb_services.png")
		

		TB_services = self.left_top_toolbar.AddLabelTool( wx.ID_ANY, u"tool", TB_services_icon)
		
		self.left_top_toolbar.Realize() 

		left_TB_sizer.Add( self.left_top_toolbar, 0, wx.EXPAND, 5 )
		
		self.left_bot_toolbar = wx.ToolBar( self.LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.left_bot_toolbar.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )

		
		TB_projects_icon = wx.Bitmap("img/tb_projects.png")
		

		TB_projects = self.left_bot_toolbar.AddLabelTool( wx.ID_ANY, u"tool", TB_projects_icon)
		
		
		TB_sales_icon = wx.Bitmap("img/tb_sales.png")
		

		TB_sales = self.left_bot_toolbar.AddLabelTool( wx.ID_ANY, u"tool", TB_sales_icon)
		
		
		TB_companies_icon = wx.Bitmap("img/tb_companies.png")
		

		TB_companies = self.left_bot_toolbar.AddLabelTool( wx.ID_ANY, u"tool", TB_companies_icon)

	
		self.left_bot_toolbar.Realize() 

		left_TB_sizer.Add( self.left_bot_toolbar, 0, wx.EXPAND, 5 )
		left_sizer.Add(left_TB_sizer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 0 )
		
		self.text_Filter = wx.StaticText( self.LeftPanel, wx.ID_ANY, "    Filters:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_Filter.Wrap( -1 )
		self.text_Filter.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.text_Filter.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )
		left_sizer.Add( self.text_Filter, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.static_line_1 = wx.StaticLine( self.LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.static_line_1.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )

		left_sizer.Add( self.static_line_1, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.filter_panel = wx.Panel(self.LeftPanel)
		self.filter_panel.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )



		#######      FILTER PANEL LAYOUT ########## ####### ####### ####### 
		####### ####### ####### ####### ####### ####### ####### ####### 
		filter_panel_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.filter_panel_layout = wx.Panel( self.filter_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		filter_panel_layout_sizer = wx.GridBagSizer( 0, 0 )
		filter_panel_layout_sizer.SetFlexibleDirection( wx.BOTH )
		filter_panel_layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sort_columns_label = wx.StaticText( self.filter_panel_layout, wx.ID_ANY, u"By column:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sort_columns_label.Wrap( -1 )
		filter_panel_layout_sizer.Add( self.sort_columns_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 3 ), wx.LEFT|wx.TOP, 10 )
		
		sort_columns_choiceChoices = []
		self.sort_columns_choice = wx.Choice( self.filter_panel_layout, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sort_columns_choiceChoices, 0 )
		self.sort_columns_choice.SetSelection( 0 )
		self.sort_columns_choice.SetMinSize( wx.Size( 150,-1 ) )
		
		filter_panel_layout_sizer.Add( self.sort_columns_choice, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.LEFT|wx.TOP, 10 )
		
		sort_mode_choiceChoices = [ u"Ascending", u"Descending" ]
		self.sort_mode_choice = wx.RadioBox( self.filter_panel_layout, wx.ID_ANY, u"Sort", wx.DefaultPosition, wx.DefaultSize, sort_mode_choiceChoices, 1, 0 )
		self.sort_mode_choice.SetSelection( 0 )
		filter_panel_layout_sizer.Add( self.sort_mode_choice, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.LEFT|wx.TOP, 15 )
		
		self.sort_search_delimiter = wx.StaticLine( self.filter_panel_layout, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		filter_panel_layout_sizer.Add( self.sort_search_delimiter, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )
		
		self.find_label = wx.StaticText( self.filter_panel_layout, wx.ID_ANY, u"Search:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.find_label.Wrap( -1 )
		filter_panel_layout_sizer.Add( self.find_label, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 15 )
		
		self.find_label_1 = wx.StaticText( self.filter_panel_layout, wx.ID_ANY, u"Label 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.find_label_1.Wrap( -1 )
		filter_panel_layout_sizer.Add( self.find_label_1, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 10 )
		
		self.find_field_1 = wx.TextCtrl( self.filter_panel_layout, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		filter_panel_layout_sizer.Add( self.find_field_1, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.find_label_2 = wx.StaticText( self.filter_panel_layout, wx.ID_ANY, u"Label 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.find_label_2.Wrap( -1 )
		filter_panel_layout_sizer.Add( self.find_label_2, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 10 )
		
		self.find_field_2 = wx.TextCtrl( self.filter_panel_layout, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		filter_panel_layout_sizer.Add( self.find_field_2, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.find_label_3 = wx.StaticText( self.filter_panel_layout, wx.ID_ANY, u"Label 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.find_label_3.Wrap( -1 )
		filter_panel_layout_sizer.Add( self.find_label_3, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 10 )
		
		self.find_field_3 = wx.TextCtrl( self.filter_panel_layout, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		filter_panel_layout_sizer.Add( self.find_field_3, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.filter_panel_layout.SetSizer( filter_panel_layout_sizer )
		self.filter_panel_layout.Layout()
		filter_panel_layout_sizer.Fit( self.filter_panel_layout )
		filter_panel_sizer.Add( self.filter_panel_layout, 1, wx.EXPAND, 5 )
		
		
		self.filter_panel.SetSizer( filter_panel_sizer )
		self.filter_panel.Layout()
		filter_panel_sizer.Fit( self.filter_panel )




		########## ####### ####### ####### ####### ####### ####### ####### ####### 
		####### ####### ####### ####### ####### ####### ####### ####### ####### 
		####### ####### ####### ####### ####### ####### ####### ####### ####### 

		left_sizer.Add( self.filter_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.LeftPanel.SetSizer( left_sizer )
		self.LeftPanel.Layout()
		left_sizer.Fit( self.LeftPanel )
		main_sizer.Add( self.LeftPanel, 0, wx.EXPAND, 5 )
		
		self.static_line_2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		self.static_line_2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		main_sizer.Add( self.static_line_2, 0, wx.EXPAND, 5 )
		
		hsizer = wx.BoxSizer( wx.VERTICAL )
		
		######## TOOLBARUL DE SUS ############################################################
		######################################################################################

		self.top_toolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
		self.top_toolbar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.top_toolbar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		
		add_client_icon = wx.Bitmap("img/add_client.png")
		
		add_client_tb = self.top_toolbar.AddLabelTool( wx.ID_ANY, "tool", 
			add_client_icon, longHelp= "Add a new client")

		
		add_product_icon = wx.Bitmap("img/add_product.png")
		add_product_tb = self.top_toolbar.AddLabelTool(wx.ID_ANY, "tool",
			add_product_icon, longHelp = 'Add a new product')
		

		
		add_service_icon =  wx.Bitmap("img/add_service.png")
		add_service_tb = self.top_toolbar.AddLabelTool(wx.ID_ANY, "tool",
			add_service_icon, longHelp = 'Add a new service')
		

		self.top_toolbar.AddSeparator()

		
		add_project_icon = wx.Bitmap("img/add_project.png")
		add_project_tb = self.top_toolbar.AddLabelTool( wx.ID_ANY, "tool", 
			add_project_icon, longHelp = "Add a new project")
		
		
		
		add_sale_icon = wx.Bitmap("img/add_sale.png")
		
		add_sale_tb = self.top_toolbar.AddLabelTool( wx.ID_ANY, "tool", 
			add_sale_icon, longHelp = "Add a new sale")

		
		add_company_icon = wx.Bitmap("img/add_company.png")
		
		add_company_tb = self.top_toolbar.AddLabelTool(wx.ID_ANY, "tool",
			add_company_icon, longHelp = "Add a new company")

		self.top_toolbar.AddSeparator()


		edit_icon = wx.Bitmap("img/edit_icon.png")
		self.edit_tb = self.top_toolbar.AddLabelTool( wx.ID_ANY, "tool", 
			edit_icon, longHelp = "Edit")
		self.edit_tb.Enable(False)

		remove_icon = wx.Bitmap("img/remove_icon.png")
		self.remove_tb = self.top_toolbar.AddLabelTool( wx.ID_ANY, "tool", 
			remove_icon, longHelp = "Remove")
		self.remove_tb.Enable(False)

		self.top_toolbar.AddSeparator()


		self.top_toolbar.Realize() 

		#######################################################################################
		
		hsizer.Add( self.top_toolbar, 0, wx.EXPAND, 5 )
		
		self.static_line_3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		hsizer.Add( self.static_line_3, 0, wx.ALL|wx.EXPAND, 3)
		

		self.Table = DBTable(self)

		hsizer.Add( self.Table, 2, wx.EXPAND, 5 )
		
		
		main_sizer.Add( hsizer, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( main_sizer )
		self.Layout()

		########### MENU SI STATUS BAR ############################################
		###########################################################################

		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.statusBar.SetFieldsCount(2)
		self.SetStatusWidths([-3, -1])

		# We're going to use a timer to drive a 'clock' in the last
		# field.
		self.timer = wx.PyTimer(self.Notify)
		self.timer.Start(1000)
		self.Notify()

		self.MenuBar = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		# self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Ajutor", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu1.AppendItem( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		self.m_menu1.AppendSeparator()
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		

		self.Bind(wx.EVT_MENU, self.OnExit, self.m_menuItem3)
		self.Bind(wx.EVT_MENU, self.OnAbout, self.m_menuItem2)
		self.MenuBar.Append( self.m_menu1, u"Menu" ) 
		
		self.SetMenuBar( self.MenuBar )
		
		
		self.Centre( wx.BOTH )

		self.selected_row = None

		self.database =  Database('databases/it_services.sqlite')
		self.OnTB_Clients(1)
 		######################################################################################
 		######################################################################################
 		##########      BIND   EVENTS    ####################################################
 		self.Bind(wx.EVT_TOOL, self.OnTB_Clients,  TB_clients)
 		self.Bind(wx.EVT_TOOL, self.OnTB_Products, TB_products)
 		self.Bind(wx.EVT_TOOL, self.OnTB_Services, TB_services)
 		self.Bind(wx.EVT_TOOL, self.OnTB_Projects, TB_projects)
 		self.Bind(wx.EVT_TOOL, self.OnTB_Sales,    TB_sales)
  		self.Bind(wx.EVT_TOOL, self.OnTB_Companies, TB_companies)
 		self.Bind(wx.EVT_TOOL, self.OnAddClient,   add_client_tb)
 		self.Bind(wx.EVT_TOOL, self.OnAddProject,  add_project_tb)
 		self.Bind(wx.EVT_TOOL, self.OnAddSale,     add_sale_tb)
 		self.Bind(wx.EVT_TOOL, self.OnAddProduct,  add_product_tb)
 		self.Bind(wx.EVT_TOOL, self.OnAddService,  add_service_tb)
 		self.Bind(wx.EVT_TOOL, self.OnAddCompany,  add_company_tb)
 		self.Bind(wx.EVT_TOOL, self.OnEdit, self.edit_tb)
  		self.Bind(wx.EVT_TOOL, self.OnRemove, self.remove_tb)
 		self.Bind(gridlib.EVT_GRID_CMD_SELECT_CELL, self.OnCellSelect, self.Table)
 		self.Bind(gridlib.EVT_GRID_COL_SIZE, self.OnCellDeselect, self.Table)
  		self.Bind(gridlib.EVT_GRID_ROW_SIZE, self.OnCellDeselect, self.Table)
 		self.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnEdit, self.Table)
  		self.Bind(wx.EVT_RADIOBOX, self.OnSortTable, self.sort_mode_choice)
  		self.Bind(wx.EVT_CHOICE, self.OnSortTable, self.sort_columns_choice)
  		self.Bind(wx.EVT_TEXT, self.OnSearch, self.find_field_1)
   		self.Bind(wx.EVT_TEXT, self.OnSearch, self.find_field_2)
  		self.Bind(wx.EVT_TEXT, self.OnSearch, self.find_field_3)
  		self.Bind(wx.EVT_CLOSE, self.OnExit)

	

  	def OnExit(self, event):
		dial = wx.MessageDialog(None, 'Are you sure?', 'Warning', 
			wx.OK | wx.CANCEL | wx.ICON_QUESTION)
		#dial.SetOKCancelLabels('OK', 'Anuleaza')
		result = dial.ShowModal()
		if result == wx.ID_OK:
			self.Destroy()
		else:
			return

	def OnAbout(self, event):
		box = AboutBox(self)
		box.Show()

	def OnTB_Clients(self, event):
		global CURRENT_TABLE, CURRENT_TABLE_DATA
		self.text_Filter.SetLabel('     Filter: Clients')
		self.text_Filter.GetParent().Layout()
		self.OnCellDeselect(None)
		CURRENT_TABLE_DATA = self.database.GetClients()
		self.Table.PutItems(CURRENT_TABLE_DATA)
		translate(CURRENT_TABLE_DATA[1], columns_dictionary)
		CURRENT_TABLE = 'Clients'
		if event != None:
			self.InitPanel()
		self.OnSortTable(None)

	def OnTB_Products(self, event):
		global CURRENT_TABLE, CURRENT_TABLE_DATA
		self.text_Filter.SetLabel('     Filter: Products')
		self.text_Filter.GetParent().Layout()
		self.OnCellDeselect(None)
		CURRENT_TABLE_DATA = self.database.GetProducts()
		self.Table.PutItems(CURRENT_TABLE_DATA)
		translate(CURRENT_TABLE_DATA[1], columns_dictionary)
		CURRENT_TABLE = 'Products'
		if event != None:
			self.InitPanel()
		self.OnSortTable(None)

	def OnTB_Services(self, event):
		global CURRENT_TABLE, CURRENT_TABLE_DATA
		self.text_Filter.SetLabel('     Filter: Services')
		self.text_Filter.GetParent().Layout()
		self.OnCellDeselect(None)
		CURRENT_TABLE_DATA = self.database.GetServices()
		self.Table.PutItems(CURRENT_TABLE_DATA)
		translate(CURRENT_TABLE_DATA[1], columns_dictionary)
		CURRENT_TABLE = 'Services'
		if event != None:
			self.InitPanel()
		self.OnSortTable(None)

	def OnTB_Projects(self, event):
		global CURRENT_TABLE, CURRENT_TABLE_DATA
		self.text_Filter.SetLabel('     Filter: Projects')
		self.text_Filter.GetParent().Layout()
		self.OnCellDeselect(None)
		CURRENT_TABLE_DATA = self.database.GetProjects()
		translate(CURRENT_TABLE_DATA[1], columns_dictionary)
		self.Table.PutItems(CURRENT_TABLE_DATA)
		CURRENT_TABLE = 'Projects'
		if event != None:
			self.InitPanel()
		self.OnSortTable(None)

	def OnTB_Sales(self, event):
		global CURRENT_TABLE, CURRENT_TABLE_DATA
		self.text_Filter.SetLabel('     Filter: Sales')
		self.text_Filter.GetParent().Layout()
		self.OnCellDeselect(None)
		CURRENT_TABLE_DATA = self.database.GetSales()
		translate(CURRENT_TABLE_DATA[1], columns_dictionary)
		self.Table.PutItems(CURRENT_TABLE_DATA)
		CURRENT_TABLE = 'Sales'
		if event != None:
			self.InitPanel()	
		self.OnSortTable(None)

	def OnTB_Companies(self, event):
		global CURRENT_TABLE, CURRENT_TABLE_DATA
		self.text_Filter.SetLabel('     Filter: Companis')
		self.text_Filter.GetParent().Layout()
		self.OnCellDeselect(None)
		CURRENT_TABLE_DATA = self.database.GetCompanies()
		translate(CURRENT_TABLE_DATA[1], columns_dictionary)
		self.Table.PutItems(CURRENT_TABLE_DATA)
		CURRENT_TABLE = 'Companies'
		if event != None:
			self.InitPanel()
		self.OnSortTable(None)



	def InitPanel(self):
		self.sort_columns_choice.SetItems(CURRENT_TABLE_DATA[1])
		self.sort_columns_choice.SetSelection(0)
		self.sort_mode_choice.SetSelection(0)

		def set_labels(l1, l2, l3):
			self.find_label_1.SetLabel(l1)
			self.find_label_2.SetLabel(l2)
			self.find_label_3.SetLabel(l3)

		if CURRENT_TABLE == 'Clients':
			set_labels('ID', 'First Name', 'Last Name')
		elif CURRENT_TABLE == 'Products':
			set_labels('ID', 'Serial', 'Name')
		elif CURRENT_TABLE == 'Projects':
			set_labels('ID', 'Engineer', 'Reg. date')
		elif CURRENT_TABLE == 'Sales':
			set_labels('ID', 'Saler', 'Date')
		elif CURRENT_TABLE == 'Companies':
			set_labels('ID', 'Name', 'Address')
		elif CURRENT_TABLE == 'Services':
			set_labels('ID', 'Type', 'Price')



	def OnAddClient(self, event):
		client_frame = AddClientFrame(self, 'Add Client', 'Add', None)

	def OnAddProject(self, event):
		project_frame = AddProjectFrame(self, 'Add Project', 'Add', 'None')

	def OnAddSale(self, event):
		sale_frame = AddSaleFrame(self, 'Add Sale', 'Add', 'None')

	def OnAddProduct(self, event):
		product_frame = AddProductFrame(self, 'Add Product', 'Add', 'None')

	def OnAddService(self, event):
		service_frame = AddServiceFrame(self, 'Add Service', 'Add', 'None')

	def OnAddCompany(self, event):
		company_frame = AddCompanyFrame(self, 'Add Company', 'Add', 'None')


	def OnRemove(self, event):
		
		dial = wx.MessageDialog(None, 'Are you sure?', 'Warning', 
			wx.OK | wx.CANCEL | wx.ICON_QUESTION)
		#dial.SetOKCancelLabels('OK', 'Cancel')
		result = dial.ShowModal()
		if result == wx.ID_OK:
			self.database.DeleteItem(self.selected_row[0], CURRENT_TABLE)
		else:
			return
		if CURRENT_TABLE == 'Clients':
			self.OnTB_Clients(None)
		elif CURRENT_TABLE == 'Products':
			self.OnTB_Products(None)
		elif CURRENT_TABLE == 'Projects':
			self.OnTB_Projects(None)
		elif CURRENT_TABLE == 'Sales':
			self.OnTB_Sales(None)
		elif CURRENT_TABLE == 'Services':
			self.OnTB_Services(None)
		elif CURRENT_TABLE == 'Companies':
			self.OnTB_Companies(None)


	def Notify(self):
		t = time.localtime(time.time())
		st = time.strftime("%d-%b-%Y   %H:%M:%S", t)
		self.statusBar.SetStatusText(st, 1)

	def OnCellSelect(self, event):
		try:
			self.selected_row =  self.Table.table.data[event.GetRow()]
		except IndexError:
			self.OnCellDeselect(None)
			return
		if self.edit_tb.IsEnabled():
			return
		self.edit_tb.Enable(True)
		self.remove_tb.Enable(True)
		self.top_toolbar.Realize()

	def OnCellDeselect(self, event):
		self.selected_row = None
		if not self.edit_tb.IsEnabled():
			return
		self.edit_tb.Enable(False)
		self.remove_tb.Enable(False)
		self.top_toolbar.Realize()

	def OnSortTable(self, event):
		self.OnCellDeselect(None)
		key = self.sort_columns_choice.GetSelection()
		
		def get_key(item):
			return item[key]

		if self.sort_mode_choice.GetSelection() == 0:
			CURRENT_TABLE_DATA[0].sort(None, get_key)
		else:
			CURRENT_TABLE_DATA[0].sort(None, get_key, True)
		self.Table.PutItems(CURRENT_TABLE_DATA)
		self.OnSearch(None)

	def OnSearch(self, event):
		self.OnCellDeselect(None)
		val1 = self.find_field_1.GetValue()
		val2 = self.find_field_2.GetValue()
		val3 = self.find_field_3.GetValue()


		dkeys = [0, 1, 2]
		if CURRENT_TABLE == 'Projects' or CURRENT_TABLE == 'Sales':
			dkeys = [0, 1, 4]

		new_items = []
		new_data = []
		for data in CURRENT_TABLE_DATA[0]:
			if compare(val1, data[dkeys[0]]) and compare(val2, data[dkeys[1]]) and compare(val3, data[dkeys[2]]):
				new_data.append(data)
		new_items.append(new_data)
		new_items.append(CURRENT_TABLE_DATA[1])
		self.Table.PutItems(new_items)


	def __del__( self ):
		pass


############## ON EDIT OPTIONS 

	def OnEdit(self, event):
		
		options               = {}
		options['id']         = self.selected_row[0]
		
		if CURRENT_TABLE == 'Clients':
			frame = AddClientFrame(self, 'Edit Client', 'Edit', options)
		elif CURRENT_TABLE == 'Projects':
			frame = AddProjectFrame(self, 'Edit Project', 'Edit', options)
		elif CURRENT_TABLE == 'Services':
			options['description'] = self.selected_row[1]
			options['price']       = self.selected_row[2]
			frame = AddServiceFrame(self, 'Edit Service', 'Edit', options)
		elif CURRENT_TABLE == 'Products':
			frame = AddProductFrame(self, 'Edit Product', 'Edit', options)
		elif CURRENT_TABLE == 'Sales':
			frame = AddSaleFrame(self, 'Edit Sale', 'Edit', options)
		elif CURRENT_TABLE == 'Companies':
			frame = AddCompanyFrame(self, 'Edit Company', 'Edit', options)



















class AddClientFrame ( wx.Frame ):
	

	def __init__( self, parent, title, mode, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, 
			pos = wx.DefaultPosition, size = wx.Size( 450, 400 ), 
			style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.mode = mode
		self.options = options
		self.parent = parent


		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.SetBackgroundColour( wx.Colour( 242, 245, 255 ))
		
		layout_sizer = wx.GridBagSizer( 0, 0 )
		layout_sizer.SetFlexibleDirection( wx.BOTH )
		layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.top_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"General Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.top_label.Wrap( -1 )
		layout_sizer.Add( self.top_label, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lname_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Last Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lname_label.Wrap( -1 )
		layout_sizer.Add( self.lname_label, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lname_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lname_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.lname_field, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.fname_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"First name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fname_label.Wrap( -1 )
		layout_sizer.Add( self.fname_label, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.fname_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fname_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.fname_field, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.comp_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Company:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.comp_label.Wrap( -1 )
		layout_sizer.Add( self.comp_label, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		comp_choiceChoices = []
		self.comp_choice = wx.ListBox( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comp_choiceChoices, 0 )
		self.comp_choice.SetMinSize( wx.Size( 150,90 ) )
		
		layout_sizer.Add( self.comp_choice, wx.GBPosition( 1, 4 ), wx.GBSpan( 3, 2 ), wx.ALL, 5 )
		
		self.comp_add_ctrl = wx.HyperlinkCtrl( self.main_panel, wx.ID_ANY, u"Add Company", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		layout_sizer.Add( self.comp_add_ctrl, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.separator = wx.StaticLine( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		layout_sizer.Add( self.separator, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
		
		self.bottom_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Contacts", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bottom_label.Wrap( -1 )
		layout_sizer.Add( self.bottom_label, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.phone_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Phone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phone_label.Wrap( -1 )
		layout_sizer.Add( self.phone_label, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.phone_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phone_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.phone_field, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.gsm_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"GSM:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gsm_label.Wrap( -1 )
		layout_sizer.Add( self.gsm_label, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.gsm_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gsm_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.gsm_field, wx.GBPosition( 7, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.mail_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"e-mail:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mail_label.Wrap( -1 )
		layout_sizer.Add( self.mail_label, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.mail_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mail_field.SetMaxLength( 40 ) 
		self.mail_field.SetMaxSize( wx.Size( 100,-1 ) )
		
		layout_sizer.Add( self.mail_field, wx.GBPosition( 8, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.addr_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addr_label.Wrap( -1 )
		layout_sizer.Add( self.addr_label, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.addr_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addr_field.SetMaxLength( 30 ) 
		self.addr_field.SetMaxSize( wx.Size( 120,-1 ) )
		
		layout_sizer.Add( self.addr_field, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.city_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.city_label.Wrap( -1 )
		layout_sizer.Add( self.city_label, wx.GBPosition( 7, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.city_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.city_field.SetMaxLength( 20 ) 
		self.city_field.SetMaxSize( wx.Size( 120,-1 ) )
		
		layout_sizer.Add( self.city_field, wx.GBPosition( 7, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.ok_button = wx.Button( self.main_panel, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.ok_button, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cancel_button, wx.GBPosition( 10, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.main_panel.SetSizer( layout_sizer )
		self.main_panel.Layout()
		layout_sizer.Fit( self.main_panel )
		main_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( main_sizer )
		self.Layout()
		self.statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.statusbar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.Centre( wx.BOTH )
##################################################################################

		self.statusbar.SetStatusText('    Fill the fields ')
		## Leaga evenimentele 
		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)
		self.Bind(wx.EVT_HYPERLINK, self.OnAddCompany, self.comp_add_ctrl)

		self.Init()

		self.MakeModal(True)
		self.Show()
	
	def __del__( self ):
		pass

	def Init(self):
		
		companies = self.parent.database.GetCompanies()
		self.companies_choices = {}
		for company in companies[0]:
			self.companies_choices[company[1]+ ' - ' + company[2]] = company[0]
		self.comp_choice.SetItems(self.companies_choices.keys())


		if self.mode == 'Add' or self.mode == 'AddP':
			self.ok_button.SetLabel('Add')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/add_client.png"))
			self.SetIcon(icon)
		
		elif self.mode == 'Edit':
			self.ok_button.SetLabel('Salveaza')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/edit_client.png"))
			self.SetIcon(icon)

			self.client_id = self.options['id']
			edit_client = self.parent.database.GetClient(self.client_id)
			self.fname_field.SetValue(edit_client[2])
			self.lname_field.SetValue(edit_client[1])
			company_id = edit_client[3]

			# selectam compania din lista
			try:
				comp_name_adress = self.parent.database.GetCompany_name_addr(company_id)
				row = self.comp_choice.FindString(comp_name_adress)
				self.comp_choice.SetSelection(row)
			except:
				pass
			
			self.phone_field.SetValue(edit_client[4])
			self.gsm_field.SetValue(edit_client[5])
			self.addr_field.SetValue(edit_client[6])
			self.city_field.SetValue(edit_client[7])
			self.mail_field.SetValue(edit_client[8])



	def OnPressOk(self, event):
		
		# extragem informatia 
		last_name  = self.lname_field.GetValue()
		first_name = self.fname_field.GetValue()
		phone      = self.phone_field.GetValue()
		gsm        = self.gsm_field.GetValue()
		mail       = self.mail_field.GetValue()
		city       = self.city_field.GetValue()
		address    = self.addr_field.GetValue()

		try:
			company_name = self.comp_choice.GetString(self.comp_choice.GetSelection())	
			company_id =   self.companies_choices[company_name]
		except wx._core.PyAssertionError:
			company_id = None

		# mai intii verificam daca sunt introduse campurile obligatorii

		if first_name == '':
			self.fname_label.SetForegroundColour((255,0,0)) 
		else:
			self.fname_label.SetForegroundColour((0,0,0)) 
		if last_name == '':
			self.lname_label.SetForegroundColour((255,0,0)) 
		else:
			self.lname_label.SetForegroundColour((0,0,0)) 

		if first_name == '' or last_name == '':
			self.statusbar.SetStatusText(' Fill the required fields')
			self.Refresh()
			return
		client = [last_name, first_name, company_id, phone, gsm, mail, address, city]
		None_toEmptyString(client)

		if self.mode == 'Add' or self.mode == 'AddP':
			self.parent.database.InsertClient(client)
			# update parent frame
			if self.mode == 'AddP':
				self.options["parent_frame"].Init()
				row = self.options["parent_frame"].client_choice.FindString(
					last_name + ' ' + first_name)
				self.options["parent_frame"].client_choice.SetSelection(row)

		elif self.mode == 'Edit':
			self.parent.database.UpdateClient(self.client_id, client)
		
		if CURRENT_TABLE == 'Clients':
			self.parent.OnTB_Clients(None)
		self.OnExit(None)

	def OnAddCompany(self, event):
		options = {}
		options['parent_frame'] = self
		company = AddCompanyFrame(self.parent, 'Add Company', 'AddP', options)

	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()
















class AddProjectFrame ( wx.Frame ):
	
	def __init__( self, parent, title, mode, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, 
			title = title, pos = wx.DefaultPosition, size = wx.Size( 520,330 ), 
			style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.mode = mode
		self.parent = parent
		self.options = options

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_Panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_Panel.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )
		
		self.layout_sizer = wx.GridBagSizer( 0, 0 )
		self.layout_sizer.SetFlexibleDirection( wx.BOTH )
		self.layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.client_label = wx.StaticText( self.main_Panel, wx.ID_ANY, u"Client: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.client_label.Wrap( -1 )
		self.layout_sizer.Add( self.client_label, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.worker_label = wx.StaticText( self.main_Panel, wx.ID_ANY, "Engineer :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.worker_label.Wrap( -1 )
		self.layout_sizer.Add( self.worker_label, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.pr_date = wx.DatePickerCtrl( self.main_Panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_SPIN )
		self.layout_sizer.Add( self.pr_date, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.deadline_date = wx.DatePickerCtrl( self.main_Panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_SPIN )
		self.layout_sizer.Add( self.deadline_date, wx.GBPosition( 4, 5 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
		
		self.pr_date_label = wx.StaticText( self.main_Panel, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pr_date_label.Wrap( -1 )
		self.layout_sizer.Add( self.pr_date_label, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.main_Panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.layout_sizer.Add( self.m_staticText20, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.deadline_date_label = wx.StaticText( self.main_Panel, wx.ID_ANY, u"Due Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.deadline_date_label.Wrap( -1 )
		self.layout_sizer.Add( self.deadline_date_label, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		client_choiceChoices = []
		self.client_choice = wx.ListBox( self.main_Panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, client_choiceChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT )
		self.client_choice.SetMinSize( wx.Size( 150,70 ) )
		self.client_choice.SetMaxSize( wx.Size( 150,70 ) )
		
		self.layout_sizer.Add( self.client_choice, wx.GBPosition( 1, 3 ), wx.GBSpan( 2, 1 ), wx.ALL, 5 )
		
		worker_choiceChoices = []
		self.worker_choice = wx.ListBox( self.main_Panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, worker_choiceChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT )
		self.worker_choice.SetMinSize( wx.Size( 130,70 ) )
		self.worker_choice.SetMaxSize( wx.Size( 80,70 ) )
		
		self.layout_sizer.Add( self.worker_choice, wx.GBPosition( 1, 6 ), wx.GBSpan( 2, 3 ), wx.ALL, 5 )
		
		self.add_client_ctrl = wx.HyperlinkCtrl( self.main_Panel, wx.ID_ANY, u"Add Client", wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		self.layout_sizer.Add( self.add_client_ctrl, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.main_Panel, wx.ID_ANY, u"Description :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.layout_sizer.Add( self.m_staticText16, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.serial_label = wx.StaticText( self.main_Panel, wx.ID_ANY, u"Serial:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serial_label.Wrap( -1 )
		self.layout_sizer.Add( self.serial_label, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.pr_name_label = wx.StaticText( self.main_Panel, wx.ID_ANY, u"Product Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pr_name_label.Wrap( -1 )
		self.layout_sizer.Add( self.pr_name_label, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.pr_name_field = wx.TextCtrl( self.main_Panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_WORDWRAP )
		self.pr_name_field.SetMaxLength( 50 ) 
		self.layout_sizer.Add( self.pr_name_field, wx.GBPosition( 4, 3 ), wx.GBSpan( 2, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.fault_field = wx.TextCtrl( self.main_Panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_WORDWRAP )
		self.fault_field.SetMaxLength( 70 ) 
		self.layout_sizer.Add( self.fault_field, wx.GBPosition( 6, 3 ), wx.GBSpan( 4, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.ok_button = wx.Button( self.main_Panel, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.layout_sizer.Add( self.ok_button, wx.GBPosition( 6, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_Panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.layout_sizer.Add( self.cancel_button, wx.GBPosition( 7, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.serial_field = wx.TextCtrl( self.main_Panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.layout_sizer.Add( self.serial_field, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
		
		
		self.main_Panel.SetSizer( self.layout_sizer )
		self.main_Panel.Layout()
		self.layout_sizer.Fit( self.main_Panel )
		main_sizer.Add( self.main_Panel, 1, wx.EXPAND, 5 )
		
		
		self.Init()
		
		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )


		## Leaga evenimentele
		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_HYPERLINK, self.OnAddClient, self.add_client_ctrl)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)

		self.MakeModal(True)
		self.Show()
	
	def __del__( self ):
		pass

	def Init(self):

		# initializam tabelul cu clienti
		clients = self.parent.database.GetClients()
		self.client_choices = {}
		for client in clients[0]:
			self.client_choices[client[1]+ ' ' + client[2]] = client[0]
		self.client_choice.SetItems(self.client_choices.keys())


		# initializam tabelul cu ingineri
		workers = self.parent.database.GetWorkers()
		self.worker_choices = {}
		for worker in workers[0]:
			self.worker_choices[worker[1]+ ' ' + worker[2]] = worker[0]
		self.worker_choice.SetItems(self.worker_choices.keys())

		if self.mode == 'Add':
			
			self.ok_button.SetLabel('Add')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/add_project.png"))
			self.SetIcon(icon)
		
		elif self.mode == 'Edit':

			self.finalize_project_ctrl = wx.HyperlinkCtrl( self.main_Panel, wx.ID_ANY, u"Finish", 
				wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
			
			self.layout_sizer.Add( self.finalize_project_ctrl, wx.GBPosition( 6, 4 ), 
				wx.GBSpan( 1, 3 ), wx.ALL, 5 )

			self.Bind(wx.EVT_HYPERLINK, self.OnFinish, self.finalize_project_ctrl)
			self.ok_button.SetLabel('Save')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/edit_project.png"))
			self.SetIcon(icon)

			self.project_id = self.options["id"]

			self.edit_project  = self.parent.database.GetProject(self.project_id)

			client_id = self.edit_project[1]
			worker_id = self.edit_project[9]
			
			# selectam clientul
			for client in self.client_choices:
				if self.client_choices[client] == client_id:
					row = self.client_choice.FindString(client)
					self.client_choice.SetSelection(row)
					break

			# selectam inginerul	
			for worker in self.worker_choices:
				if self.worker_choices[worker] == worker_id:
					row = self.worker_choice.FindString(worker)
					self.worker_choice.SetSelection(row)
					break

			# adaugam campurile necesare

			self.serial_field.SetValue(self.edit_project[2])
			self.pr_name_field.SetValue(self.edit_project[3])
			self.fault_field.SetValue(self.edit_project[4])

			date_obj = wx.DateTime()
			date_obj.ParseFormat(self.edit_project[6], '%Y-%m-%d')
			self.pr_date.SetValue(date_obj)
			date_obj.ParseFormat(self.edit_project[7], '%Y-%m-%d')
			self.deadline_date.SetValue(date_obj)



	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()

	def OnAddClient(self, event):
		options = {}
		options['parent_frame'] = self
		client_frame = AddClientFrame(self.parent, 'Add Client', 'AddP', options)

	def OnPressOk(self, event):
		
		try:
			client_name = self.client_choice.GetString(self.client_choice.GetSelection())	
			client_id =   self.client_choices[client_name]
		except wx._core.PyAssertionError:
			client_id = None

		try:
			worker_name = self.worker_choice.GetString(self.worker_choice.GetSelection())	
			worker_id =   self.worker_choices[worker_name]
		except wx._core.PyAssertionError:
			worker_id = None


		serial        = self.serial_field.GetValue()
		pr_name       = self.pr_name_field.GetValue()
		fault         = self.fault_field.GetValue()
		pr_date       = self.pr_date.GetValue().Format('%Y-%m-%d')
		deadline_date = self.deadline_date.GetValue().Format('%Y-%m-%d')

		# verificam daca sunt introduse campurile obligatorii

		if client_id == None:
			self.client_label.SetForegroundColour((255,0,0)) 
		else:
			self.client_label.SetForegroundColour((0,0,0)) 
		if worker_id == None:
			self.worker_label.SetForegroundColour((255,0,0)) 
		else:
			self.worker_label.SetForegroundColour((0,0,0)) 
		if pr_name == '':
			self.pr_name_label.SetForegroundColour((255,0,0)) 
		else:
			self.pr_name_label.SetForegroundColour((0,0,0))
		
		if client_id == None or worker_id == None or pr_name == '':
			self.Refresh()
			return


		project = [client_id, serial, pr_name, fault, None, pr_date, deadline_date,
		  None, worker_id, None,  None, None, None, None, None]
		None_toEmptyString(project)

		if self.mode == 'Add':
			self.project_id = self.parent.database.InsertProject(project)
		elif self.mode == 'Edit':
			self.parent.database.UpdateProject(self.project_id, project)		
		

		dial = wx.MessageDialog(None, 'Dou you want to print out input file?', 'Warning', 
			wx.OK | wx.CANCEL | wx.ICON_QUESTION)
		#dial.SetOKCancelLabels('OK', 'Anuleaza')
		result = dial.ShowModal()
		if result == wx.ID_OK:
			data = self.parent.database.GetProjectLarge(self.project_id)
			self.parent.PRINTER.Print(data, 'service_intrare.png', 'service_intrare')


		if CURRENT_TABLE == 'Projects':
			self.parent.OnTB_Projects(None)



		self.OnExit(None)

	def OnFinish(self, event):
		self.edit_project  = self.parent.database.GetProject(self.project_id)
		finalize_frame = OrderFrame(self.parent, self.edit_project)













class AddServiceFrame ( wx.Frame ):
	
	def __init__( self, parent, title, mode, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 391,211 ), 
			style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.parent = parent
		self.mode = mode
		self.options = options

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		layout_sizer = wx.GridBagSizer( 0, 0 )
		layout_sizer.SetFlexibleDirection( wx.BOTH )
		layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.description_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Service Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description_label.Wrap( -1 )
		layout_sizer.Add( self.description_label, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.description_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.description_field.SetMinSize( wx.Size( 200,50 ) )
		
		layout_sizer.Add( self.description_field, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
		
		self.price_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_label.Wrap( -1 )
		layout_sizer.Add( self.price_label, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.price_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.price_field, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.ok_button = wx.Button( self.main_panel, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.ok_button, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cancel_button, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.main_panel.SetSizer( layout_sizer )
		self.main_panel.Layout()
		layout_sizer.Fit( self.main_panel )
		main_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.Init()

		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)


		self.MakeModal(True)
		self.Show()
	
	def __del__( self ):
		pass

	def Init(self):
		
		if self.mode == 'Add':
			self.ok_button.SetLabel('Add')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/add_service.png"))
			self.SetIcon(icon)

		elif self.mode == 'Edit':
			self.ok_button.SetLabel('Save')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/edit_service.png"))
			self.SetIcon(icon)

			self.service_id = self.options["id"]
			self.description_field.SetValue(self.options['description'])
			self.price_field.SetValue(self.options['price'])

	def OnPressOk(self, event):

		description = self.description_field.GetValue()
		price = self.price_field.GetValue()

		service = [description, price]

		if self.mode == 'Add':
			self.parent.database.InsertService(service)
		elif self.mode == 'Edit':
			self.parent.database.UpdateService(self.service_id, service)

		if CURRENT_TABLE == 'Services':
			self.parent.OnTB_Services(None)

		self.OnExit(None)


	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()


















class AddProductFrame ( wx.Frame ):
	
	def __init__( self, parent, title, mode, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title,
			pos = wx.DefaultPosition, size = wx.Size( 420,299 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.parent = parent
		self.mode = mode
		self.options = options

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )
		
		layout_sizer = wx.GridBagSizer( 0, 0 )
		layout_sizer.SetFlexibleDirection( wx.BOTH )
		layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.serial_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Serial:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serial_label.Wrap( -1 )
		layout_sizer.Add( self.serial_label, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.name_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_label.Wrap( -1 )
		layout_sizer.Add( self.name_label, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.name_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		self.serial_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serial_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.serial_field, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		layout_sizer.Add( self.name_field, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.price_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_label.Wrap( -1 )
		layout_sizer.Add( self.price_label, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.price_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.price_field, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.stock_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Stock:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_label.Wrap( -1 )
		layout_sizer.Add( self.stock_label, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.stock_spin_ctrl = wx.SpinCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 10000, 0)
		layout_sizer.Add( self.stock_spin_ctrl, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.warrant_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Warranty:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.warrant_label.Wrap( -1 )
		layout_sizer.Add( self.warrant_label, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.warrant_spin_ctrl = wx.SpinCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 36, 0 )
		layout_sizer.Add( self.warrant_spin_ctrl, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.description_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description_label.Wrap( -1 )
		layout_sizer.Add( self.description_label, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.description_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.description_field.SetMinSize( wx.Size( 200,70 ) )
		
		layout_sizer.Add( self.description_field, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
		
		self.ok_button = wx.Button( self.main_panel, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.ok_button, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cancel_button, wx.GBPosition( 6, 6 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		
		self.main_panel.SetSizer( layout_sizer )
		self.main_panel.Layout()
		layout_sizer.Fit( self.main_panel )
		main_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		self.serial_field.SetFocus()
		
		self.Init()
		
		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)

		self.MakeModal(True)
		self.Show()
	
	def __del__( self ):
		pass

	def Init(self):
		
		if self.mode == 'Add':	
			self.selected_product = None
			self.ok_button.SetLabel('Add')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/add_product.png"))
			self.SetIcon(icon)

		elif self.mode == 'Edit':
			self.selected_product = None
			self.ok_button.SetLabel('Save')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/edit_product.png"))
			self.SetIcon(icon)

			self.product_id = self.options["id"]
			edit_product = self.parent.database.GetProduct(self.product_id)

			self.serial_field.SetValue(edit_product[1])
			self.name_field.SetValue(edit_product[2])
			self.price_field.SetValue(edit_product[3])
			self.warrant_spin_ctrl.SetValue(edit_product[4])
			self.description_field.SetValue(edit_product[5])
			self.stock_spin_ctrl.SetValue(edit_product[6])


	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()

	def OnPressOk(self, event):
		
		serial      = self.serial_field.GetValue()
		name        = self.name_field.GetValue()
		price       = self.price_field.GetValue()
		description = self.description_field.GetValue()
		stock       = self.stock_spin_ctrl.GetValue()
		warrant     = self.warrant_spin_ctrl.GetValue()

		# verificam daca sunt introduse campurile obligatorii

		if serial == '':
			self.serial_label.SetForegroundColour((255,0,0)) 
		else:
			self.serial_label.SetForegroundColour((0,0,0)) 
		if name == '':
			self.name_label.SetForegroundColour((255,0,0)) 
		else:
			self.name_label.SetForegroundColour((0,0,0)) 
		if price == '':
			self.price_label.SetForegroundColour((255,0,0)) 
		else:
			self.price_label.SetForegroundColour((0,0,0)) 

		if serial == '' or name == '' or price == '':
			self.Refresh()
			return


		product = [serial, name, price, warrant, description, stock]
		None_toEmptyString(product)

		if self.mode == 'Add':
			self.parent.database.InsertProduct(product)
		elif self.mode == 'Edit':
			self.parent.database.UpdateProduct(self.product_id, product)
		
		if CURRENT_TABLE == 'Products':
			self.parent.OnTB_Products(None)
		
		self.OnExit(None)


















class AddSaleFrame ( wx.Frame ):
	
	def __init__( self, parent, title, mode, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title,  
			pos = wx.DefaultPosition, size = wx.Size( 538,392 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.parent  = parent
		self.mode    = mode
		self.options = options


		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		layout_sizer = wx.GridBagSizer( 0, 0 )
		layout_sizer.SetFlexibleDirection( wx.BOTH )
		layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.client_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Client: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.client_label.Wrap( -1 )
		layout_sizer.Add( self.client_label, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.worker_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Saler:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.worker_label.Wrap( -1 )
		layout_sizer.Add( self.worker_label, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.s_date = wx.DatePickerCtrl( self.main_panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_SPIN )
		layout_sizer.Add( self.s_date, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
		
		self.s_date_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.s_date_label.Wrap( -1 )
		layout_sizer.Add( self.s_date_label, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		client_choiceChoices = []
		self.client_choice = wx.ListBox( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, client_choiceChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT )
		self.client_choice.SetMinSize( wx.Size( 150,70 ) )
		self.client_choice.SetMaxSize( wx.Size( 150,70 ) )
		
		layout_sizer.Add( self.client_choice, wx.GBPosition( 1, 3 ), wx.GBSpan( 2, 1 ), wx.ALL, 5 )
		
		worker_choiceChoices = []
		self.worker_choice = wx.ListBox( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, worker_choiceChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT )
		self.worker_choice.SetMinSize( wx.Size( 130,70 ) )
		self.worker_choice.SetMaxSize( wx.Size( 80,70 ) )
		
		layout_sizer.Add( self.worker_choice, wx.GBPosition( 1, 6 ), wx.GBSpan( 2, 4 ), wx.ALL, 5 )
		
		self.comments_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Comments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.comments_label.Wrap( -1 )
		layout_sizer.Add( self.comments_label, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
		
		self.add_client_ctrl = wx.HyperlinkCtrl( self.main_panel, wx.ID_ANY, u"Add Client", wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		layout_sizer.Add( self.add_client_ctrl, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.products_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Product:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.products_label.Wrap( -1 )
		layout_sizer.Add( self.products_label, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.products_list = DBList(self.main_panel, size = ( 230,170 ))
		layout_sizer.Add( self.products_list, wx.GBPosition( 4, 1 ), wx.GBSpan( 4, 3 ), wx.ALL, 5 )
		
		self.products = self.parent.database.GetProductsShort()
		translate(self.products[1], columns_dictionary)
		self.products_list.PutItems(self.products)

		self.comments_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,115 ), 0 )
		layout_sizer.Add( self.comments_field, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 5 ), wx.LEFT, 10 )
		
		self.serial_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serial_field.SetMaxLength( 15 ) 
		layout_sizer.Add( self.serial_field, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		# icon = wx.Bitmap("img/warrant_icon.png")		
		# self.print_warrant_button = wx.BitmapButton( self.main_panel, wx.ID_ANY, icon, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		# layout_sizer.Add(self.print_warrant_button, wx.GBPosition(8, 4))

		self.ok_button = wx.Button( self.main_panel, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.ok_button, wx.GBPosition( 8, 5 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cancel_button, wx.GBPosition( 8, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.main_panel.SetSizer( layout_sizer )
		self.main_panel.Layout()
		layout_sizer.Fit( self.main_panel )
		main_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.Init()

		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)
		self.Bind(wx.EVT_HYPERLINK, self.OnAddClient, self.add_client_ctrl)
		self.Bind(wx.EVT_TEXT, self.OnSerialChange, self.serial_field)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.products_list)

		self.MakeModal(True)
		self.Show()
	
	def __del__( self ):
		pass

	def Init(self):
		# initializam tabelul cu clienti
		clients = self.parent.database.GetClients()
		self.client_choices = {}
		for client in clients[0]:
			self.client_choices[client[1]+ ' ' + client[2]] = client[0]
		self.client_choice.SetItems(self.client_choices.keys())


		# initializam tabelul cu ingineri
		workers = self.parent.database.GetWorkers()
		self.worker_choices = {}
		for worker in workers[0]:
			self.worker_choices[worker[1]+ ' ' + worker[2]] = worker[0]
		self.worker_choice.SetItems(self.worker_choices.keys())

		
		if self.mode == 'Add':
			
			self.selected_product = None
			self.ok_button.SetLabel('Add')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/add_sale.png"))
			self.SetIcon(icon)

		elif self.mode == 'Edit':
			self.selected_product = None
			self.ok_button.SetLabel('Save')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/edit_sale.png"))
			self.SetIcon(icon)


			self.sale_id = self.options["id"]

			self.edit_sale  = self.parent.database.GetSale(self.sale_id)

			client_id = self.edit_sale[3]
			worker_id = self.edit_sale[1]
			
			# selectam clientul
			for client in self.client_choices:
				if self.client_choices[client] == client_id:
					row = self.client_choice.FindString(client)
					self.client_choice.SetSelection(row)
					break

			# selectam inginerul	
			for worker in self.worker_choices:
				if self.worker_choices[worker] == worker_id:
					row = self.worker_choice.FindString(worker)
					self.worker_choice.SetSelection(row)
					break

			# # adaugam campurile necesare

			date_obj = wx.DateTime()
			date_obj.ParseFormat(self.edit_sale[4], '%Y-%m-%d')
			self.s_date.SetValue(date_obj)

			comments = self.edit_sale[5]
			self.comments_field.SetValue(comments)
			sel_product = self.parent.database.GetProduct(self.edit_sale[2])
			self.serial_field.SetValue(sel_product[1])
			self.OnSerialChange(None)


	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()

	def OnAddClient(self, event):
		options = {}
		options['parent_frame'] = self
		client_frame = AddClientFrame(self.parent, 'Add Client', 'AddP', options)

	def OnSerialChange(self, event):

		ser = self.serial_field.GetValue()
		new_items = []
		new_products = []
		for product in self.products[0]:
			if compare(ser, product[0]):
				new_products.append(product)
		new_items.append(new_products)
		new_items.append(self.products[1])
		self.products_list.PutItems(new_items)

	def OnPressOk(self, event):
		
		try:
			client_name = self.client_choice.GetString(self.client_choice.GetSelection())	
			client_id =   self.client_choices[client_name]
		except wx._core.PyAssertionError:
			client_id = None

		try:
			worker_name = self.worker_choice.GetString(self.worker_choice.GetSelection())	
			worker_id =   self.worker_choices[worker_name]
		except wx._core.PyAssertionError:
			worker_id = None

		# verificam daca sunt introduse campurile obligatorii

		if client_id == None:
			self.client_label.SetForegroundColour((255,0,0)) 
		else:
			self.client_label.SetForegroundColour((0,0,0)) 
		if worker_id == None:
			self.worker_label.SetForegroundColour((255,0,0)) 
		else:
			self.worker_label.SetForegroundColour((0,0,0)) 
		if self.selected_product == None:
			self.products_label.SetForegroundColour((255,0,0)) 
		else:
			self.products_label.SetForegroundColour((0,0,0)) 	

		if client_id == None or worker_id == None or self.selected_product == None:
			self.Refresh()
			return

		product_id = self.parent.database.GetProductID(self.selected_product)
		s_date       = self.s_date.GetValue().Format('%Y-%m-%d')
		comments = self.comments_field.GetValue()

		sale = [worker_id, product_id, client_id, s_date,  comments]
		None_toEmptyString(sale)

		if self.mode == 'Add':
			self.parent.database.InsertSale(sale)
			self.parent.database.RemoveFromStock(product_id)
		elif self.mode == 'Edit':
			self.parent.database.UpdateSale(self.sale_id, sale)



		dial = wx.MessageDialog(None, 'Do you want to print warranty document?', 'Warning', 
			wx.OK | wx.CANCEL | wx.ICON_QUESTION)
		#dial.SetOKCancelLabels('OK', 'Anuleaza')
		result = dial.ShowModal()
		if result == wx.ID_OK:
			data = self.parent.database.GetSaleLarge(self.sale_id)
			self.parent.PRINTER.Print(data, 'garantie.png', 'garantie_vinzare')

		if CURRENT_TABLE == 'Sales':
			self.parent.OnTB_Sales(None)

		self.OnExit(None)

	def OnItemSelected(self, event):
		current_item = event.m_itemIndex
		self.selected_product =  self.products_list.GetItemText(current_item)
		event.Skip()
























class AddCompanyFrame ( wx.Frame ):
	
	def __init__( self, parent, title, mode, options):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, 
			pos = wx.DefaultPosition, size = wx.Size( 358,350 ), 
			style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.parent = parent
		self.options = options
		self.mode = mode

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(  wx.Colour( 242, 245, 255 ))
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.SetBackgroundColour(  wx.Colour( 242, 245, 255 ) )
		
		layout_sizer = wx.GridBagSizer( 0, 0 )
		layout_sizer.SetFlexibleDirection( wx.BOTH )
		layout_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.name_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_label.Wrap( -1 )
		layout_sizer.Add( self.name_label, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.name_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_field.SetMaxLength( 50 ) 
		self.name_field.SetMinSize( wx.Size( 200,-1 ) )
		
		layout_sizer.Add( self.name_field, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.addr_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addr_label.Wrap( -1 )
		layout_sizer.Add( self.addr_label, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.addr_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addr_field.SetMaxLength( 50 ) 
		layout_sizer.Add( self.addr_field, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.phone_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Phone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phone_label.Wrap( -1 )
		layout_sizer.Add( self.phone_label, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.phone_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phone_field.SetMaxLength( 30 ) 
		layout_sizer.Add( self.phone_field, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.static_line = wx.StaticLine( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		layout_sizer.Add( self.static_line, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )
		
		self.bank_data_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Bank data:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bank_data_label.Wrap( -1 )
		layout_sizer.Add( self.bank_data_label, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cod_fisc_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Fiscal code:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cod_fisc_label.Wrap( -1 )
		layout_sizer.Add( self.cod_fisc_label, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cod_fisc_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cod_fisc_field, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.cod_decont_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Debit code:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cod_decont_label.Wrap( -1 )
		layout_sizer.Add( self.cod_decont_label, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cod_decont_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cod_decont_field, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.cod_banc_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Bank code:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cod_banc_label.Wrap( -1 )
		layout_sizer.Add( self.cod_banc_label, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cod_banc_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cod_banc_field, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.cod_trez_label = wx.StaticText( self.main_panel, wx.ID_ANY, u"Cod trezozorial:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cod_trez_label.Wrap( -1 )
		layout_sizer.Add( self.cod_trez_label, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cod_trez_field = wx.TextCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cod_trez_field, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.ok_button = wx.Button( self.main_panel, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.ok_button, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self.main_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		layout_sizer.Add( self.cancel_button, wx.GBPosition( 9, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.main_panel.SetSizer( layout_sizer )
		self.main_panel.Layout()
		layout_sizer.Fit( self.main_panel )
		main_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )

########################################################################

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Bind(wx.EVT_BUTTON, self.OnPressOk, self.ok_button)
		self.Bind(wx.EVT_BUTTON, self.OnExit, self.cancel_button)

		self.Init()

		self.MakeModal(True)
		self.Show()
	

	def __del__( self ):
		pass


	def OnPressOk(self, event):

		name = self.name_field.GetValue()
		address = self.addr_field.GetValue()
		phone = self.phone_field.GetValue()
		cod_fisc = self.cod_fisc_field.GetValue()
		cod_decont = self.cod_decont_field.GetValue()
		cod_bancar = self.cod_banc_field.GetValue()
		cod_trez = self.cod_trez_field.GetValue()

		if name == '':
			self.name_label.SetForegroundColour((255,0,0)) 
		else:
			self.name_label.SetForegroundColour((0,0,0)) 

		if name == '':
			self.Refresh()
			return

		company = [name, address, phone, cod_fisc, cod_decont, cod_bancar, cod_trez]
		None_toEmptyString(company)

		if self.mode == 'Add' or self.mode == 'AddP':
			self.parent.database.InsertCompany(company)

			if self.mode == 'AddP':
				self.options["parent_frame"].Init()
				row = self.options["parent_frame"].comp_choice.FindString(
					name + ' - ' + address)
				self.options["parent_frame"].comp_choice.SetSelection(row)

		elif self.mode == 'Edit':
			self.parent.database.UpdateCompany(self.company_id, company)



		if CURRENT_TABLE == 'Companies':
			self.parent.OnTB_Companies(None)

		self.OnExit(None)



	def OnExit(self, event):
		self.MakeModal(False)
		self.Destroy()


	def Init(self):
		
		if self.mode == 'Add' or self.mode == 'AddP':	
			self.ok_button.SetLabel('Adauga')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/add_company.png"))
			self.SetIcon(icon)

		elif self.mode == 'Edit':
			self.selected_product = None
			self.ok_button.SetLabel('Salveaza')
			icon = wx.Icon('img/gg.ico', wx.BITMAP_TYPE_ICO)
			icon.CopyFromBitmap(wx.Bitmap("img/edit_company.png"))
			self.SetIcon(icon)

			self.company_id = self.options['id']
			edit_company = self.parent.database.GetCompany(self.company_id)
			self.name_field.SetValue(edit_company[1])
			self.addr_field.SetValue(edit_company[2])
			self.phone_field.SetValue(edit_company[3])
			self.cod_fisc_field.SetValue(edit_company[4])
			self.cod_decont_field.SetValue(edit_company[5])
			self.cod_banc_field.SetValue(edit_company[6])
			self.cod_trez_field.SetValue(edit_company[7])


def None_toEmptyString(data):

	for i in range(len(data)):
		if data[i] == None:
			data[i] = ''

def EmptyString_toNone(data):
	
	for i in range(len(data)):
		if data[i] == '':
			data[i] = None
			

def translate(data, dictionary):

	for i in range(len(data)):
		try:
			data[i] = dictionary[data[i]]
		except:
			data[i] = data[i]

def compare(a, b):

	if a == '' or b == '':
		return True
	int_cmp = False
	if type(a) == type(1) or type(b) == type(1):
		int_cmp = True
	if int_cmp:
		try:
			return int(a) == int(b)
		except:
			return False
	n = min(len(a), len(b))
	for i in range(n):
		if a[i] != b[i]:
			return False
	return True