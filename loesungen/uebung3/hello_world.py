#!/usr/bin/env python

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Hello World",
                          size=(800, 600))
        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()



# Oder so:

# class MainFrame(wx.Frame):
#     def __init__(self, title, size):
#         wx.Frame.__init__(self, parent=None, title=title, size=size)
#         self.Show(True)

# app = wx.PySimpleApp()
# frame = MainFrame("Hello World", (800, 600))
# app.MainLoop()
