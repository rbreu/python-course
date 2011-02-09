#!/usr/bin/env python

try:
    import readline
except ImportError:
    print "Module readline not available. Going on without."
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")


raw_input("Python-Ausdruck eingeben: ")


# Auch wenn wir sicher sind, dass Windows-Systeme das Modul readline nicht
# besitzen und andere Systeme schon: Eigentlich wollen wir ja nur testen,
# ob es das Modul gibt oder nicht, das Betriebssystem ist und recht
# egal. Es koennte sein, dass sich ein Windows-Besitzer selber ein
# solches Modul geschrieben hat, welches wir dann benutzen koennen. In der
# tat kann man sich im Internet ein readline-Modul fuer Windows herunterladen.
#
# Andererseits koennte sich jemand auf einem Linux-System ein kleinstmoegliche
# Python-Installation zusammengebastelt haben, in der das readline-Modul fehlt,
# und es waere unschoen, wenn user Programm wegen eines nicht essenziell
# wichtigen Modules dort dann nicht laufen wuerde.
#
# FAZIT: Statt mit if-Abfragen Ausnahmen zu vermeiden, ist es meist flexibler,
# die Ausnahmen geeignet zu behandeln, da so Eigenschaften abprueft werden,
# die wir wirklich brauchen, waehrend die if-Abragen oft Annahmen des
# Programmieres enthalten, die in ungewoehlichen Situationen nicht unbedingt
# zutreffend sind.
