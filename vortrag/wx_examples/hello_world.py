#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Hello World")
        self.Show(True)

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
