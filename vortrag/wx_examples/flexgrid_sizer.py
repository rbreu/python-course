#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="BoxSizer")
        panel = wx.Panel(parent=self)
        grid = wx.FlexGridSizer(3, 3, 5, 5)

        for i in range(9):
            button = wx.Button(parent=panel, label=str(i))
            grid.Add(button, flag=wx.EXPAND)

        grid.AddGrowableRow(idx=2, proportion=1)
        grid.AddGrowableCol(idx=2, proportion=1)

        panel.SetSizer(grid)
        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
