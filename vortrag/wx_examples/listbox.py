#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)
        options = ["One", "Two", "Three"]
        self.list = wx.ListBox(parent=panel, choices=options,
                               style=wx.LB_MULTIPLE)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.list)
        self.Show(True)

    def onListBox(self, evt):
        print "Your selection:", self.list.GetSelections()

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
