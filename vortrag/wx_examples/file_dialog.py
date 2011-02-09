#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)
        self.Show(True)

        dlg = wx.FileDialog(parent=panel, message="Choose a file",
                            wildcard="Python|*.py|All|*",
                            style=wx.OPEN)

        value = dlg.ShowModal()
        if value == wx.ID_OK:
            print dlg.GetPath()

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
