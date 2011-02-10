#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Text Input")
        panel = wx.Panel(parent=self)
        options = ["One", "Two", "Three"]

        # Mache radio zu einem Objektattribut, da mit wir auch
        # ausserhalb dieser Methode darauf zugreifen koennen:
        #
        # Make radio an attribute of the object so that we can
        # access it from outside of this method:
        self.radio = wx.RadioBox(parent=panel, label="Your choice",
                                 choices = options, majorDimension=1,
                                 style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.onRadioBox, self.radio)
        self.Show(True)


    def onRadioBox(self, evt):
        # Hier greifen wir auf die oben definierte Radiobox zu:
        #
        # Here we access the radio box defined above:
        print "Your selection:", self.radio.GetStringSelection()



app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
