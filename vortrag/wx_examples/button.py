#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Button Test")
        panel = wx.Panel(parent=self)
        button = wx.Button(parent=panel, label="&Click me")
        self.Bind(wx.EVT_BUTTON, self.onButton, button)
        self.Show(True)

    def onButton(self, evt):
        print "You pressed the button!"

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
