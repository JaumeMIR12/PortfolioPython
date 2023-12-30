import wx
# Para que funcione he tenido que instalar wx
# Con el comando pip install wxPython

aplicacion = wx.App()
ventana = wx.Frame(parent=None,title="Hola Mundo")
ventana.Show()
aplicacion.MainLoop()