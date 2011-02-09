#!/usr/bin/env python

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Buttons")
        panel = wx.Panel(parent=self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Oder:
        # sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel.SetSizer(sizer)

        for label in ["One", "Two", "Three"]:
            button = wx.Button(parent=panel, label=label)
            sizer.Add(button, proportion=1, flag=wx.CENTER)

        self.Show(True)




app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
