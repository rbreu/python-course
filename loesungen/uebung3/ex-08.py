#!/usr/bin/env python

import wx

class OneMenu(wx.Menu):
    """
    One popup menu.
    """

    def __init__(self, parent, items):
        """
        items: List of menu items, where one item is a list:
                  [name, status bar text, method to bind, enable flag]

        Create a separator with an empty list.
        """ 
        wx.Menu.__init__(self)
 
        for item in items:
            if item:
                menu_item = self.Append(-1, item[0], item[1])
                menu_item.Enable(item[3])
                parent.Bind(wx.EVT_MENU, item[2], menu_item)
            else:
                self.AppendSeparator()


class Editor(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, size=(800,600))

        self.filename = None
        self.text_changed = False

        self.update_title()
        self.panel = wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(parent=self.panel, style=wx.TE_MULTILINE)
        box.Add(self.text, proportion=1, flag=wx.EXPAND)
        self.Bind(wx.EVT_TEXT, self.on_change, self.text)

        self.CreateStatusBar()

        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        # Liste, welche alle Eintraege des Filemenues enthaelt:
        #
        # List which contains all entries of the file menu:
        items = [["&New\tCtrl+N", "New File", self.on_new, True],
                 ["&Open...\tCtrl+O", "Open File", self.on_open, True],
                 [], # Separator
                 ["&Save\tCtrl+S", "Save File", self.on_save, True],
                 ["&Save as...\tShift+Ctrl+S", "Save File as", self.on_save_as, True],
                 [],
                 ["&Quit\tCtrl+Q", "Exit Program", self.on_quit, True]]

        # Ein Menue aus der Liste erstellen und der Menuezeile hinzufuegen:
        #
        # Create a menu from the list and add it to the file menu:
        menubar.Append(OneMenu(self, items), "&File")

        self.panel.SetSizer(box)
        self.Show(True)


    def on_quit(self, evt):

        if self.text_changed:
            value = self.warn_dialog()
            if value == wx.ID_NO:
                return
            
        self.Close(True)


    def on_new(self, evt):

        if self.text_changed:
            value = self.warn_dialog()
            if value == wx.ID_NO:
                return

        self.filename = None
        self.text.Clear()
        self.text_changed = False
        self.update_title()
        self.SetStatusText("New File.")


    def on_open(self, evt):

        if self.text_changed:
            value = self.warn_dialog()
            if value == wx.ID_NO:
                return

        dlg = wx.FileDialog(parent=self.panel, message="Open File",
                            style=wx.OPEN)

        value = dlg.ShowModal()

        if value == wx.ID_OK:
            self.filename = dlg.GetPath()
            f = open(self.filename)
            self.text.SetValue(f.read())
            f.close()

            self.text_changed = False
            self.update_title()
            self.SetStatusText("Opened File %s." % self.filename)


    def on_save_as(self, evt):
        dlg = wx.FileDialog(parent=self.panel, message="Save File",
                            style=wx.SAVE)

        value = dlg.ShowModal()

        if value == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.save()
            self.text_changed = False
            self.update_title()

    
    def on_save(self, evt):
        try:
            self.save()
        except TypeError:
            self.on_save_as(None)


    def on_change(self, evt):
        self.text_changed = True
        self.update_title()


    def save(self):
        f = open(self.filename, "w")
        f.write(self.text.GetValue())
        f.close()
        self.SetStatusText("Saved File %s." % self.filename)
        self.text_changed = False
        self.update_title()


    def update_title(self):
        changed = "*" if self.text_changed else ""
        title = "MyEditor: %s%s" % (self.filename, changed)
        self.SetTitle(title)


    def warn_dialog(self):
        msg = "File %s is not saved. Continue?" % self.filename
        dlg = wx.MessageDialog(parent=self.panel, message=msg,
                               caption="Really Continue?",
                               style=wx.YES_NO | wx.ICON_QUESTION)
        value = dlg.ShowModal()
        return value


app = wx.PySimpleApp()
frame = Editor()
app.MainLoop()
