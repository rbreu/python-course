#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="BoxSizer")
        panel = wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        button = wx.Button(parent=panel, label="Top")
        box.Add(button, proportion=1,
                flag=wx.ALIGN_TOP|wx.ALL, border=5)

        button = wx.Button(parent=panel, label="Expand")
        box.Add(button, proportion=1,
                flag=wx.EXPAND|wx.ALL, border=5)

        button = wx.Button(parent=panel, label="Bottom")
        box.Add(button, proportion=1,
                flag=wx.ALIGN_BOTTOM|wx.ALL, border=5)

        button = wx.Button(parent=panel, label="Center")
        box.Add(button, proportion=1,
                flag=wx.ALIGN_CENTER|wx.ALL, border=5)

        panel.SetSizer(box)
        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
