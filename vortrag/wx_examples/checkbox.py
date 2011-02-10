#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)
        self.check = wx.CheckBox(parent=panel, label="Check &me")
        self.Bind(wx.EVT_CHECKBOX, self.onCheckBox, self.check)
        self.Show(True)

    def onCheckBox(self, evt):
        if self.check.IsChecked():
            print "Checked"
        else:
            print "Not Checked"

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
