#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Button Test")
        panel = wx.Panel(parent=self)
        button = wx.Button(parent=panel, label="Eins", pos=(40,100))
        button = wx.Button(parent=panel, label="Zwei", pos=(160,100))
        button = wx.Button(parent=panel, label="Drei", pos=(280,100))

        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
