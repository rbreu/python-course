#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)

        button = wx.Button(parent=panel, label="Click me")

        self.Show(True)

        msg = wx.MessageDialog(parent=panel, message="Are you ok?",
                               caption="Question",
                               style=wx.YES_NO | wx.ICON_QUESTION)

        value = msg.ShowModal()
        if value == wx.ID_YES:
            print "That's fine!"
        else:
            print "I'm sorry."


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
