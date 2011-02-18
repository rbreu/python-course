#!/usr/bin/env python

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Some Text")

        # Nicht das Panel vergessen, welches all unsere Widgets enthaelt:
        #
        # Don't forget the panel which contains all our widgets:
        panel = wx.Panel(parent=self)

        # Alle Widgets zu Kindern des Panels machen. Dadurch werden sie
        # automatisch im Panel angezeigt:
        #
        # Make all widgets childs of the panel. Thus they will be
        # automatically displayed inside the panel:
        wx.StaticText(parent=panel,
                      label="Hello\nworld!\nHow is it?",
                      style=wx.ALIGN_CENTER)
        wx.StaticText(parent=panel, label="Blah blah.", pos=(80, 80))
        wx.StaticText(parent=panel, label="More Text", pos=(100, 10))

        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()



# Gibt man den Static-Text keine Positionsangaben mit, so werden alle in
# die linke obere Ecke gezeichnet und ueberlappen. Manuelle Positionierung
# ist kompliziert und das Ergebnis passt sich nicht an verschiedene
# Fenstergroessen, Schriftarten etc an.
#
# If you omit the position parameters of the static text widgets, all of
# them will be drawn in the upper left corner and overlap. Manual
# positioning is complicated and the result doesn't adjust to different
# window  sizes, fonts etc.
