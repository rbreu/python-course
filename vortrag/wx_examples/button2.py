#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Button Test")
        panel = wx.Panel(parent=self)
        button = wx.Button(parent=panel, label="&Click me")
        self.Bind(wx.EVT_BUTTON, self.onButtonF, button)
        button.Bind(wx.EVT_BUTTON, self.onButtonB, button)
        self.Show(True)

    def onButtonF(self, evt):
        print "You pressed the button!"

    def onButtonB(self, evt):
        print "You pressed me!"
        #evt.Skip()

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
