#!/usr/bin/env python

import wx

class Editor(wx.Frame):
    """
    Haupfenster eines einfachen Texteditors.

    Main frame of a simple text editor.
    """

    
    def __init__(self):
        wx.Frame.__init__(self, parent=None, size=(800,600))

        # Dateiname zum Speichern der Satei und Darstellen in der Titelleiste:
        #
        # filename for saving the file and displaying in title bar:
        self.filename = None

        # Speicherstatus der Datei fuer Warnungen an den Anwender und zum
        # Darstellen in der Titelleiste:
        #
        # save status of the file for warnings to the user and for
        # displaying it in the title bar:
        self.text_changed = False

        # Fenstertitel setzen:
        #
        # Set window title:
        self.update_title()
        
        self.panel = wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        # Das Texteinfabefeld, im Frame zentriert und gestreckt:
        #
        # The text entry field, centred in the frame and expanded:
        self.text = wx.TextCtrl(parent=self.panel, style=wx.TE_MULTILINE)
        box.Add(self.text, proportion=1, flag=wx.EXPAND)

        # Wir wollen Textaenderungen mitbekommen:
        #
        # We want to catch text changes:
        self.Bind(wx.EVT_TEXT, self.on_change, self.text)

        # Statuszeile und Menuezeile:
        #
        # Status bar and menu bar:
        self.CreateStatusBar()

        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        # Das File-Menue:
        #
        # The file menu:
        file_menu = wx.Menu()
        menubar.Append(file_menu, "&File")
        
        new = file_menu.Append(-1, "&New\tCtrl+N", "New File")
        self.Bind(wx.EVT_MENU, self.on_new, new)

        open_ = file_menu.Append(-1, "&Open...\tCtrl+O", "Open File")
        self.Bind(wx.EVT_MENU, self.on_open, open_)

        file_menu.AppendSeparator()

        save = file_menu.Append(-1, "&Save\tCtrl+S", "Save File")
        self.Bind(wx.EVT_MENU, self.on_save, save)

        saveas = file_menu.Append(-1, "&Save as...\tShift+Ctrl+S", "Save File as")
        self.Bind(wx.EVT_MENU, self.on_save_as, saveas)

        file_menu.AppendSeparator()

        quit = file_menu.Append(-1, "&Quit\tCtrl+Q", "Exit Program")
        self.Bind(wx.EVT_MENU, self.on_quit, quit)

        self.panel.SetSizer(box)
        self.Show(True)


    def on_quit(self, evt):
        """
        Frame schliessen.
        Wenn die geoeffnete Datei nicht gespeichert ist, warne den
        Anwender.

        Close frame.
        If the opened file has not been saved yet, warn the user.
        """

        # Warne den Anwender:
        #
        # Warn the user:
        if self.text_changed:
            value = self.warn_dialog()
            if value == wx.ID_NO:
                return

        # Hier will der Anwender will wirklich fortfahren
        #
        # At this point, the user really wants to continue
        self.Close(True)


    def on_new(self, evt):
        """
        Neue Datei -- Inhalt des Textfeldes loeschen.
        Wenn die bisher geoeffnete Datei nicht gespeichert ist, warne den
        Anwender.

        New file -- remove content of text entry field.
        If the opened file has not been saved yet, warn the user.
        """

        # Warne den Anwender:
        #
        # Warn the user:
        if self.text_changed:
            value = self.warn_dialog()
            if value == wx.ID_NO:
                return

        # Hier will der Anwender will wirklich fortfahren
        #
        # At this point, the user really wants to continue

        # Achtung, bei einer neuen Datei gibt es ersteinmal keinen zu ihr
        # gehoerenden Dateinamen!
        #
        # Beware, for a new file, we don't have an associated file name yet!
        self.filename = None
        
        self.text.Clear()
        self.text_changed = False
        self.update_title()
        self.SetStatusText("New File.")


    def on_open(self, evt):
        """
        Oeffne eine Datei, welche der Anwender mittels File-Dialog aussucht.
        Wenn die bisher geoeffnete Datei nicht gespeichert ist, warne den
        Anwender.

        Open a file which the user pick via a file dialog.
        If the afore opened file has not been saved yet, warn the user.
        """

        # Warne den Anwender:
        #
        # Warn the user:
        if self.text_changed:
            value = self.warn_dialog()
            if value == wx.ID_NO:
                return

        # Hier will der Anwender will wirklich fortfahren
        #
        # At this point, the user really wants to continue

        # File-Open-Dialog, Parent ist das Panel
        #
        # File open dialog, its parent is the panel
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
        """
        Speichere eine Datei unter einem Namen, den der Anwender
        mittels File-Dialog aussucht.
        """
        
        
        # File-Save-Dialog, Parent ist das Panel
        #
        # File save dialog, its parent is the panel
        dlg = wx.FileDialog(parent=self.panel, message="Save File",
                            style=wx.SAVE)

        value = dlg.ShowModal()

        if value == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.save()
            self.text_changed = False
            self.update_title()

    
    def on_save(self, evt):
        """
        Speichere eine Datei unter dem alten Namen. Wenn die Datei keinen
        Namen hat, oeffne einen File-Dialog.

        Save the file under the old name. If the file doesn't have a
        name yet, open a file dialog.
        """
        
        try:
            self.save()
        except TypeError:
            # Datei konnte nicht gepeichert werden, da es noch keinen
            # zugehoerigen Dateinamen gibt
            #
            # File couldn't be saved since ther isn't an associated
            # file name yet
            self.on_save_as(None)


    def on_change(self, evt):
        """
        Wird aufgerufen, wenn das Textfeld veraendert wird.

        Gets called when the text changes.
        """

        self.text_changed = True
        self.update_title()


    def save(self):
        """
        Das eigentliche Speichern einer Datei.

        The actual saving of the file.
        """

        # In eigene Funktion ausgelagert, da wir es an mehreren Stellen
        # benoetigen
        #
        # Put into its own function since we need it several times.
        
        f = open(self.filename, "w")
        # Das wirft TypeError, wenn self.filname==None
        #
        # Throws TypeError when self.filname==None
        
        f.write(self.text.GetValue())
        f.close()
        self.SetStatusText("Saved File %s." % self.filename)
        self.text_changed = False
        self.update_title()


    def update_title(self):
        """
        Fenstertitel gemaess aktuellem Dateinamen und Speicherstatus
        setzen.

        Set window title according to current file name and save status.
        """
        
        # in eigene Funktion ausgelagert, da wir es an mehreren Stellen
        # benoetigen
        #
        # Put into its own function since we need it several times.

        changed = "*" if self.text_changed else ""
        title = "MyEditor: %s%s" % (self.filename, changed)
        self.SetTitle(title)


    def warn_dialog(self):
        """
        Eine MessageBox, die "Really Continue?" fragt.
        """

        # in eigene Funktion ausgelagert, da wir es an mehreren Stellen
        # benoetigen
        #
        # Put into its own function since we need it several times.
        
        msg = "File %s is not saved. Continue?" % self.filename
        dlg = wx.MessageDialog(parent=self.panel, message=msg,
                               caption="Really Continue?",
                               style=wx.YES_NO | wx.ICON_QUESTION)
        value = dlg.ShowModal()
        return value


app = wx.PySimpleApp()
frame = Editor()
app.MainLoop()
