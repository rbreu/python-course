#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Hello World")
        panel = wx.Panel(parent=self)
        text = wx.StaticText(parent=panel, label="How are you?")
        self.Show(True)

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
