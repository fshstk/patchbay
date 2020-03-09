################################################################################
# OpcodeStudioPatch.py
# Part of patchbay_matrix package
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# Used to encode channel routing commands sent to the Opcode Studio 128X
# Note that the Studio 128X offers a large degree of granularity in which
# signals to route. For the sake of simplicity, all of these are either on or
# off here, since this level of customisation is not needed.
################################################################################

from bitarray import bitarray

class OpcodeStudio128Patch:
    def __init__(self, port_in, port_out, enable = True):
        self.port_in = port_in
        self.port_out = port_out

        self.note_on_off = enable
        self.pitch_bend = enable
        self.sysex = enable
        self.timecode = enable
        self.real_time = enable
        self.control_change = enable
        self.key_aftertouch = enable
        self.program_change = enable
        self.active_sense_reset = enable
        self.channel_pressure = enable
        self.sys_common = enable

        self.channel_bump = 0
        self.channels = [enable]*16

    def encode(self):
        return(
            bytes([
                self.port_in,
                self.port_out,
                self.channel_bump]) +

            bitarray([
                False,
                self.note_on_off,
                self.key_aftertouch,
                self.control_change,
                self.program_change,
                self.channel_pressure,
                self.pitch_bend,
                self.sysex,

                False,
                self.timecode,
                self.sys_common,
                self.real_time,
                self.active_sense_reset,
                False,
                False,
                False,

                False,
                False,
                False,
                False,
                self.channels[15],  # ch 16
                self.channels[14],  # ch 15
                self.channels[13],  # ch 14
                self.channels[12],  # ch 13

                False,
                False,
                False,
                False,
                self.channels[11],  # ch 12
                self.channels[10],  # ch 11
                self.channels[9],   # ch 10
                self.channels[8],   # ch 09

                False,
                False,
                False,
                False,
                self.channels[7],   # ch 08
                self.channels[6],   # ch 07
                self.channels[5],   # ch 06
                self.channels[4],   # ch 05

                False,
                False,
                False,
                False,
                self.channels[3],   # ch 04
                self.channels[2],   # ch 03
                self.channels[1],   # ch 02
                self.channels[0]    # ch 01
            ]).tobytes())