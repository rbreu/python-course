#!/usr/bin/env python

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Buttons")
        panel = wx.Panel(parent=self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)

        button = wx.Button(parent=panel, label="Click Me!")

        # Button so hinzufuegen, dass er in alle Richgungen gedehnt wird:
        sizer.Add(button, proportion=1, flag=wx.EXPAND)

        self.Show(True)




app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
