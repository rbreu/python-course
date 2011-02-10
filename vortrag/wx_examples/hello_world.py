#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Hello World")
        self.Show(True)

        self.Bind(wx.EVT_KEY_DOWN, self.onKey, self)
        

    def onKey(self, evt):
        print evt, dir(evt)

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
