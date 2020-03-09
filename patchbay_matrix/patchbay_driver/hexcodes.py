################################################################################
# hexcodes.py
# Part of patchbay_matrix package
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# These are all the hex codes needed to communicate with the Opcode Studio 128X
# (Taken from the SysEx Reference file)
################################################################################

init_prefix = b'\xf5\x7e'
command_prefix = b'\xf0\x00\x00\x37\x06'
command_suffix = b'\xf7'

commands = {
    'init'                  : b'\x6e',
    'deinit'                : b'\x6f',

    'set_routing'           : b'\x57',
    'get_routing'           : b'\x58',                  # NOTE: unconfirmed

    'program_select'        : b'\x60',
    'program_store'         : b'\x62',                  # NOTE: unconfirmed
    'program_set_number'    : b'\x65',                  # NOTE: unconfirmed
    'program_get_number'    : b'\x66',                  # NOTE: unconfirmed

    'test_ram'              : b'\x14\x00',              # NOTE: unconfirmed
    'get_rom_checksum'      : b'\x15\x00',              # NOTE: unconfirmed
    'get_rom_version'       : b'\x16\x00',              # NOTE: unconfirmed

    'smpte_sync'            : b'\x20\x00\x7e\x01',      # NOTE: unconfirmed
    'smpte_stripe'          : b'\x20\x00\x7e\x02',      # NOTE: unconfirmed
    'smpte_start_bcd'       : b'\x70\x00',              # NOTE: unconfirmed
    'smpte_start_binary'    : b'\x71\x00',              # NOTE: unconfirmed
    'smpte_set_time'        : b'\x72\x00\x00',          # NOTE: unconfirmed
    'smpte_frame_override'  : b'\x75\x00',              # NOTE: unconfirmed
    'smpte_stop'            : b'\x76\x00',              # NOTE: unconfirmed
    'smpte_set_bits'        : b'\x77\x00',              # NOTE: unconfirmed
    'smpte_get_bits'        : b'\x01\x00\x00\x26',      # NOTE: unconfirmed
    'smpte_set_parameters'  : b'\x7c\x00',              # NOTE: unconfirmed
    'smpte_get_parameters'  : b'\x7d'                   # NOTE: unconfirmed
}