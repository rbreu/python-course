#!/usr/bin/env python

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Buttons")
        panel = wx.Panel(parent=self)

        close_button = wx.Button(parent=panel, label="&Close")
        # Das & ermoeglicht, den Button mit Alt+C zu klicken
        #
        # The & enables clickinng the button by pressing Alt+C

        # Welche Funktion soll ausgefuehrt werden, wenn der Button
        # geklickt wird?
        #
        # Which function is going to be executed on button presses?
        self.Bind(wx.EVT_BUTTON, self.on_close, close_button)

        click_button = wx.Button(parent=panel, label="C&lick Me!", pos=(0,40))
        self.Bind(wx.EVT_BUTTON, self.on_click, click_button)

        click_button2 = wx.Button(parent=panel, label="Click &Me!", pos=(0,80))
        self.Bind(wx.EVT_BUTTON, self.on_click2, click_button2)

        self.Show(True)


    def on_close(self, evt):
        self.Close(True)


    def on_click(self, evt):
        print "You clicked me!"


    def on_click2(self, evt):
        print "Yeah!"


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
