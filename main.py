import wx
from GUI import *

APP_TITLE = 'Database-Services'
global logNULL

class MainApp(wx.App):

	def OnInit(self):

		logNULL = wx.LogNull()
		# Login frame creation
		self.login_frame = LoginFrame(None, 'Database-Services')
		if self.login_frame.ShowModal() == 1:	# if Logged
			self.frame = MainFrame(None)		# Create main frame
			self.SetTopWindow(self.frame)
			self.frame.Show()
		self.login_frame.Destroy()

		return True

if __name__ == '__main__':
	app = MainApp(False)
	app.MainLoop()
