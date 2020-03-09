################################################################################
# patchbay_driver
# Part of the patchbay_matrix package
#
# Python serial driver for Opcode Studio 128X
# Based on work done by Maxwell Pray (@synthead)
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# Currently supports routing and patch changes.
# A number of SMPTE & test commands are theoretically possible but untested,
# since I can't get the Studio 128X to send proper responses.
#
# EXAMPLE COMMANDS:
#
# MIDI Routing:
# OpcodeStudio128X.route(1, 4)                  -> MIDI routing: IN 1 ---> OUT 4
# OpcodeStudio128X.route(1, 4, enable = False)  -> MIDI routing: IN 1 -/-> OUT 4
#
# Patch Selection/Storage:
# OpcodeStudio128X.select_patch(4)
# OpcodeStudio128X.store_patch(4)
################################################################################

from .OpcodeStudio128X import OpcodeStudio128X