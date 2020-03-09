#!/usr/bin/env python3
################################################################################
# Python web interface for Opcode Studio 128X
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# Uses flask to display a (8x8) routing matrix as a web interface.
# Cells are clickable which automatically updates their status.
# Clear all and a pre-defined standard program are also available.
# Many more functions are possible (see comments in driver package), but this
# works fine for now.
################################################################################

from patchbay_matrix import app

app.run()