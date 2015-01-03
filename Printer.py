import wx
import  wx.lib.wordwrap as wordwrap

USER_NAME = ""
USER_ID   = ""

class Drawer():

    def __init__(self, data, doctype, dc):
        self.doctype = doctype
        self.dc = dc
        self.data = data

    def Draw(self):
        if self.doctype == 'service_intrare':
            self.DrawServiceIn()
        elif self.doctype == 'service_eliberare':
            self.DrawServiceOut()
        elif self.doctype == 'garantie_service':
            self.DrawWarrantService()
        elif self.doctype == 'garantie_vinzare':
            self.DrawWarrantSale()


    def DrawServiceIn(self):


        client_name_pos  = (1750, 1025)
        client_phone_pos = (1750, 1125)
        product_name_pos = (550, 1700)
        fault_pos        = (180, 2250)
        date_pos         = [(580, 850), (700, 850), (820, 850)]
        ID_pos           = (400, 1085)
        user_pos         = (650, 3157)
        
        client_name  = self.data[1][1] + ' ' + self.data[1][2]
        client_phone = self.data[1][4]
        serial       = self.data[0][2]
        product_name = self.data[0][3]
        fault        = self.data[0][4]
        date         = self.data[0][6].split('-')
        ID           = self.data[0][0]


        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        color = wx.Colour(20, 20, 20)
        self.dc.SetTextForeground(color)
        self.dc.SetFont(font)
        

        self.dc.DrawText(client_name , client_name_pos[0], client_name_pos[1])
        
        self.dc.DrawText(client_phone, client_phone_pos[0], client_phone_pos[1])


        text = wordwrap.wordwrap(product_name, 1100, self.dc)
        text = text.split('\n')
        i = 1
        self.dc.DrawText('Serial: ' + serial, product_name_pos[0], product_name_pos[1])

        for line in text:
            self.dc.DrawText(line, product_name_pos[0], product_name_pos[1] + i*50)
            i = i + 1

        text = wordwrap.wordwrap(fault, 2200, self.dc)
        text = text.split('\n')
        i = 0
        for line in text:
            self.dc.DrawText(line, fault_pos[0], fault_pos[1] + i*50)
            i = i + 1


        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.dc.SetFont(font)
        self.dc.DrawText(date[2], date_pos[0][0], date_pos[0][1])
        self.dc.DrawText(date[1], date_pos[1][0], date_pos[1][1])
        self.dc.DrawText(date[0], date_pos[2][0], date_pos[2][1])
        self.dc.DrawText(USER_NAME.upper(), user_pos[0], user_pos[1])

        font = wx.Font(150, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        color = wx.Colour(23, 54, 93)
        self.dc.SetTextForeground(color)
        self.dc.SetFont(font)
        self.dc.DrawText(str(ID), ID_pos[0], ID_pos[1])


    def DrawServiceOut(self):
       
        client_name_pos  = (1750, 1025)
        client_phone_pos = (1750, 1125)
        product_name_pos = (550, 1700)
        found_pos        = (180, 1520)
        date_pos         = [(580, 850), (700, 850), (810, 850)]
        return_pos       = [(580, 970), (700, 970), (810, 970)]
        user_pos         = (650, 3087)
        pieces_pos       = (1020, 1974)
        comments_pos     = (1650, 2020)
        warrant_pos      = (1850, 1945)
        worker_pos       = (2000, 2410)
        price_pos        = (680, 2907)

        client_name  = self.data[1][1] + ' ' + self.data[1][2]
        client_phone = self.data[1][4]
        found        = self.data[0][5]
        date         = self.data[0][6].split('-')
        return_date  = self.data[0][8].split('-')
        pieces       = String_toPP([self.data[0][11], self.data[0][12]])
        warrant      = self.data[0][13]
        comments     = self.data[0][14]
        price        = self.data[0][15]
        worker_name  = self.data[3][1] + ' ' + self.data[3][2] 


        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        color = wx.Colour(20, 20, 20)
        self.dc.SetTextForeground(color)
        self.dc.SetFont(font)
        

        self.dc.DrawText(client_name , client_name_pos[0], client_name_pos[1])
        
        self.dc.DrawText(client_phone, client_phone_pos[0], client_phone_pos[1])
        

        font = wx.Font(32, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.dc.SetFont(font)
        text = wordwrap.wordwrap(found, 1850, self.dc)
        text = text.split('\n')
        i = 0
        for line in text:
            self.dc.DrawText(line, found_pos[0], found_pos[1] + i*50)
            i = i + 1

        text = wordwrap.wordwrap(comments, 740, self.dc)
        text = text.split('\n')
        i = 0
        for line in text:
            self.dc.DrawText(line, comments_pos[0], comments_pos[1] + i*50)
            i = i + 1

        i = 0 
        for piece in pieces:
            self.dc.DrawText(piece[0] + ' - '  + piece[1] + ' lei', pieces_pos[0], pieces_pos[1] + i*70)
            i = i + 1


        self.dc.DrawText(worker_name, worker_pos[0], worker_pos[1])
        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.dc.SetFont(font)
        self.dc.DrawText(str(warrant) + ' luni', warrant_pos[0], warrant_pos[1])
        self.dc.DrawText(date[2], date_pos[0][0], date_pos[0][1])
        self.dc.DrawText(date[1], date_pos[1][0], date_pos[1][1])
        self.dc.DrawText(date[0], date_pos[2][0], date_pos[2][1])
        self.dc.DrawText(return_date[2], return_pos[0][0], return_pos[0][1])
        self.dc.DrawText(return_date[1], return_pos[1][0], return_pos[1][1])
        self.dc.DrawText(return_date[0], return_pos[2][0], return_pos[2][1])

        self.dc.DrawText(price, price_pos[0], price_pos[1])
        self.dc.DrawText(USER_NAME.upper(), user_pos[0], user_pos[1])

    def DrawWarrantService(self):

        return_pos  = [(580, 850), (700, 850), (810, 850)]
        type_pos    = (280, 1075)
        serial_pos  = (610, 1075)
        name_pos    = (980, 1075)
        cant_pos    = (1640, 1075)
        achit_pos   = (1860, 1075)
        warrant_pos = (750, 1530)
        
        
        return_date  = self.data[0][8].split('-')
        type_text    = "Serviciu/Reparatie"
        warrant      = self.data[0][13]
        serial       = self.data[0][2]
        product_name = self.data[0][3]
        cant         = "1 buc."
        achit    = self.data[0][15] + " lei"

       
        font = wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        color = wx.Colour(20, 20, 20)
        self.dc.SetTextForeground(color)
        self.dc.SetFont(font)

        self.dc.DrawText(type_text, type_pos[0], type_pos[1])
        self.dc.DrawText(serial, serial_pos[0], serial_pos[1])
        self.dc.DrawText(product_name, name_pos[0], name_pos[1])
        self.dc.DrawText(cant, cant_pos[0], cant_pos[1])
        self.dc.DrawText(achit, achit_pos[0], achit_pos[1])


        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.dc.SetFont(font)
        self.dc.DrawText(str(warrant) , warrant_pos[0], warrant_pos[1])
        self.dc.DrawText(return_date[2], return_pos[0][0], return_pos[0][1])
        self.dc.DrawText(return_date[1], return_pos[1][0], return_pos[1][1])
        self.dc.DrawText(return_date[0], return_pos[2][0], return_pos[2][1])


    def DrawWarrantSale(self):


        return_pos  = [(580, 850), (700, 850), (810, 850)]
        type_pos    = (280, 1075)
        serial_pos  = (610, 1075)
        name_pos    = (980, 1075)
        cant_pos    = (1640, 1075)
        achit_pos   = (1860, 1075)
        warrant_pos = (750, 1530)
        
        
        return_date  = self.data[0][4].split('-')
        type_text    = "Produs"
        warrant      = self.data[1][4]
        serial       = self.data[1][1]
        product_name = self.data[1][2]
        cant         = "1 buc."
        achit        = self.data[1][3] + " lei"

       
        font = wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        color = wx.Colour(20, 20, 20)
        self.dc.SetTextForeground(color)
        self.dc.SetFont(font)

        self.dc.DrawText(type_text, type_pos[0], type_pos[1])
        self.dc.DrawText(serial, serial_pos[0], serial_pos[1])
        self.dc.DrawText(product_name, name_pos[0], name_pos[1])
        self.dc.DrawText(cant, cant_pos[0], cant_pos[1])
        self.dc.DrawText(achit, achit_pos[0], achit_pos[1])
       



        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.dc.SetFont(font)
        self.dc.DrawText(str(warrant) , warrant_pos[0], warrant_pos[1])
        self.dc.DrawText(return_date[2], return_pos[0][0], return_pos[0][1])
        self.dc.DrawText(return_date[1], return_pos[1][0], return_pos[1][1])
        self.dc.DrawText(return_date[0], return_pos[2][0], return_pos[2][1])

class MyPrintout(wx.Printout):

    def __init__(self, data, filename, doctype):
        wx.Printout.__init__(self)
        self.data = data
        self.filename = filename
        self.doctype = doctype



    def OnPrintPage(self, page):

        dc = self.GetDC()

        #-------------------------------------------
        # One possible method of setting scaling factors...

        # Format A4
        maxX = 2480
        maxY = 3508

        # Get the size of the DC in pixels
        (w, h) = dc.GetSizeTuple()

        # Calculate a suitable scaling factor
        scaleX = float(w) / maxX
        scaleY = float(h) / maxY

        # Use x or y scaling factor, whichever fits on the DC
        actualScale = min(scaleX, scaleY)

        # Calculate the position on the DC for centering the graphic
        posX = (w - (2480 * actualScale)) / 2.0
        posY = (h - (3508 * actualScale)) / 2.0

        # Set the scale and origin
        dc.SetUserScale(actualScale, actualScale)
        dc.SetDeviceOrigin(int(posX), int(posY))


        image = wx.Bitmap("printer/%s" %self.filename)

        drawer = Drawer(self.data, self.doctype, dc)

        dc.BeginDrawing()
        dc.DrawBitmap(image, 0, 0)	# draw template
        drawer.Draw()				# draw the rest
        dc.EndDrawing()

        return True



class Printer():

    def __init__(self, parent):
        self.parent = parent
        global USER_NAME, USER_ID
        USER_NAME = self.parent.USER_NAME
        USER_ID   = self.parent.USER_ID


    def Print(self, data, filename, doctype):
        printout = MyPrintout(data, filename = filename, doctype = doctype)
        printout2 = MyPrintout(data, filename = filename, doctype = doctype) 
        printer  = wx.Printer()
        #printer.Print(self.parent, printout, True)

        preview = wx.PrintPreview(printout, printout2)
        preview_frame = wx.PreviewFrame(preview, self.parent, "Tiparirea documentului")
        preview_frame.Initialize()
        preview_frame.SetSize((600, 600))
        preview_frame.SetPosition((400, 50))
        preview_frame.Show()


# class MainFrame(wx.Frame):

#     def __init__(self, parent):
#         wx.Frame.__init__(self, parent = parent, size = (400, 400), title = 'Test Frame')
#         self.printData = wx.PrintData()
#         self.printData.SetPaperId(wx.PAPER_A4)
#         self.printData.SetPrintMode(wx.PRINT_MODE_PRINTER)
#         self.panel = wx.Panel(self)
#         self.button = wx.Button(self.panel, wx.ID_ANY, "CLICK ME!!!!", pos = (150, 150), size = (100, 100))


#         self.Bind(wx.EVT_BUTTON, self.OnPrint, self.button)
#         self.Centre()
#         self.Show()


#     def OnPrint(self, event):
#         self.printer = Printer(self)
#         self.printer.Print(None, "Page_1.png", 'service_intrare')

# if __name__ == '__main__':
#     app = wx.App(None)
#     frame = MainFrame(None)
#     app.MainLoop()


def String_toPP(data):

    parsed_piece = data[0].split('#')
    parsed_price = data[1].split('#')
    parsed_piece.pop(0)
    parsed_price.pop(0)
    parsed = []
    for i in range(len(parsed_piece)):
        parsed.append([parsed_piece[i], parsed_price[i]])
    return parsed