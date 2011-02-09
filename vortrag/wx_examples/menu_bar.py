#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Menu Demo")

        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        menu = wx.Menu()
        menubar.Append(menu, "&Menu")
        
        blah = menu.Append(-1, "&Blah\tCtrl+B", "Some explanation")
        self.Bind(wx.EVT_MENU, self.onBlah, blah)
        
        foo = menu.Append(-1, "&Foo\tCtrl+F", "Some other explanation")
        self.Bind(wx.EVT_MENU, self.onFoo, foo)

        self.CreateStatusBar()

        self.Show(True)


    def onBlah(self, evt):
        print "You selected blah."

    def onFoo(self, evt):
        print "You selected foo."


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
