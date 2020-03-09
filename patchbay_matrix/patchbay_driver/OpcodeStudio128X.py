################################################################################
# OpcodeStudio128X.py
# Part of patchbay_matrix package
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# Contains all the commands needed to initialise and interface with the
# Opcode Studio 128X
################################################################################

from serial import Serial
from time import sleep, time

from . import hexcodes # doesn't work when running this file directly >:(
from .OpcodeStudio128Patch import OpcodeStudio128Patch

class OpcodeStudio128X:
    def __init__(self, serial_port, init = True):
        self.serial = Serial()
        self.serial.port = serial_port
        self.serial.baudrate = 115200
        self.serial.timeout = 1

        if init:
            self.init()

    def __del__(self):
        self.deinit()

    def send_command(self, command, parameters = b'', use_init_prefix = False):
        try:
            self.serial.write(
                hexcodes.init_prefix + # only necessary for init, but whatever
                hexcodes.command_prefix +
                hexcodes.commands[command] +
                parameters +
                hexcodes.command_suffix)
        except KeyError:
            print("Unknown command: " + command)
            return
        # sleep(0.2)
        # return self.read_all()

    def read_all(self):
        num_bytes = self.serial.in_waiting
        data = self.serial.read(num_bytes)
        return data

    # def parse_response(self, response):
    #     data_formatted = response.hex().upper().split('F8')
    #     for element in data_formatted:
    #         if len(element) > 0:
    #             element_formatted = ''
    #             for i in range(0,len(element), 2):
    #                 element_formatted += element[i:i+2] + ' '
    #             print(element_formatted)
        
    def init(self):
        if self.serial.isOpen():
            self.deinit()

        self.serial.open()
        sleep(0.1)
        timeout = time() + 0.5
        for _ in range(4):
            while self.serial.cts is self.serial.rts:
                if time() > timeout:
                    raise TimeoutError('unable to communicate with device')
            self.serial.rts = self.serial.cts
        sleep(0.1)
        self.send_command('init')

    def deinit(self):
        if self.serial.isOpen():
            try:
                self.send_command('deinit')
            except:
                pass
            self.serial.close()

    def route(self, port_in, port_out, enable = True):
        port_settings = OpcodeStudio128Patch(port_in, port_out, enable).encode()
        self.send_command('set_routing', port_settings)

    def select_patch(self, patch):
        self.send_command('program_select', patch)

    def store_patch(self, patch):
        self.send_command('program_store', patch)

if __name__ == '__main__':
    import IPython
    try:
        x = OpcodeStudio128X('/dev/tty.usbserial')
        IPython.embed()
    except TimeoutError:
        print("Can't reach device. Check connection and/or restart the device.")