#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)
        text = wx.TextCtrl(panel, value="Default", size=(200,100),
                           style=wx.TE_MULTILINE|wx.TE_CENTER)
        
        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
