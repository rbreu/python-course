#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)
        self.Show(True)

        msg = wx.TextEntryDialog(parent=panel, message="Your name?",
                                 caption="Question", style=wx.OK)

        value = msg.ShowModal()
        if value == wx.ID_OK:
            print msg.GetValue()

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
