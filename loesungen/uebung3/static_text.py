#!/usr/bin/env python

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Some Text")

        # Nicht das Panel vergessen, welches all unsere Widgets enthaelt:
        panel = wx.Panel(parent=self)

        # Alle Widgets zu Kindern des Panels machen. Dadurch werden sie
        # automatisch im Panel angezeigt:
        wx.StaticText(parent=panel,
                      label="Hallo\nWelt!\nWie geht's?",
                      style=wx.ALIGN_CENTER)
        wx.StaticText(parent=panel, label="Lalelu", pos=(80, 80))
        wx.StaticText(parent=panel, label="Und noch ein Text", pos=(100, 10))

        self.Show(True)


app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()



# Gibt man den Static-Text keine Positionsangaben mit, so werden alle in
# die linke obere Ecke gezeichnet und ueberlappen. Manuelle Positionierung
# ist kompliziert und das Ergebnis passt sich nicht an verschiedene
# Fenstergroessen, Schriftarten etc an.
