#!/usr/bin/env python3
#
# Script to discover and report undocumented commands.

import os
import sys

parent, bindir = os.path.split(os.path.dirname(os.path.abspath(sys.argv[0])))
if os.path.exists(os.path.join(parent, 'crmsh')):
    sys.path.insert(0, parent)


from crmsh.ui_root import Root
import crmsh.help

crmsh.help.HELP_FILE = "doc/crm.8.adoc"
crmsh.help._load_help()

_IGNORED_COMMANDS = ('help', 'quit', 'cd', 'up', 'ls')

def check_help(ui):
    for name, child in ui._children.items():
        if child.type == 'command':
            try:
                h = crmsh.help.help_command(ui.name, name)
                if h.generated and name not in _IGNORED_COMMANDS:
                    print("Undocumented: %s %s" % (ui.name, name))
            except:
                print("Undocumented: %s %s" % (ui.name, name))
        elif child.type == 'level':
            h = crmsh.help.help_level(name)
            if h.generated:
                print("Undocumented: %s %s" % (ui.name, name))
            check_help(child.level)

check_help(Root())
