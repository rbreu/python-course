#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="BoxSizer")
        panel = wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        button = wx.Button(parent=panel, label="Proportion 0")
        box.Add(button, proportion=0, flag=wx.ALL, border=5)

        button = wx.Button(parent=panel, label="Proportion 1")
        box.Add(button, proportion=1, flag=wx.ALL, border=5)

        button = wx.Button(parent=panel, label="Proportion 2")
        box.Add(button, proportion=2, flag=wx.ALL, border=5)

        panel.SetSizer(box)
        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
