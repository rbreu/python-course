#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="BoxSizer")
        panel = wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        for i in ["Eins", "Zwei", "Drei"]:
            button = wx.Button(parent=panel, label=i)
            box.Add(button, proportion=1, flag=wx.ALIGN_CENTER|wx.ALL,
                    border=5)


        panel.SetSizer(box)
        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
