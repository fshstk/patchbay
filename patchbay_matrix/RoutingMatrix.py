################################################################################
# RoutingMatrix.py
# Part of patchbay_matrix package
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# Routing matrix struct for updating web interface & Opcode Studio 128X
################################################################################

from time import sleep
from .patchbay_driver import OpcodeStudio128X
from .channel_names import input_names, output_names

class RoutingMatrix:
    matrix = []

    def __init__(self, patchbay, size = 8):
        if size == 0 or size%8 != 0:
            raise IndexError("size needs to be a multiple of 8")

        self.size = size
        self.patchbay = patchbay

        for row in range(self.size):
            self.matrix.append([])
            for col in range(self.size):
                self.matrix[row].append('')

        self.clear_all(send = False)

    def send_cell(self, row, col):
        self.patchbay.route(
                    port_in = row+1,
                    port_out = col+1,
                    enable = self.matrix[row][col])

    def send_all(self):
        for row in range(self.size):
            for col in range(self.size):
                self.send_cell(row, col)
                sleep(0.005)

    def activate_cell(self, row, col, send = True):
        self.matrix[row][col] = True
        if send:
            self.send_cell(row, col)

    def disable_cell(self, row, col, send = True):
        self.matrix[row][col] = False
        if send:
            self.send_cell(row, col)

    def toggle_cell(self, row, col, send = True):
        self.matrix[row][col] = not self.matrix[row][col]
        if send:
            self.send_cell(row, col)

    def toggle_cell_by_id(self, id, send = True):
        row = id//self.size
        col = id%self.size

        self.matrix[row][col] = not self.matrix[row][col]
        if send:
            self.send_cell(row, col)
    def clear_all(self, send = True):
        for row in range(self.size):
            for col in range(self.size):
                self.matrix[row][col] = False
        if send:
            self.send_all()

    def standard_routing(self, send = True):
        self.clear_all(send = False)

        # BEGIN STANDARD ROUTING:
        # (use send = False for efficiency)
        #
        # Example #1:
        # self.activate_cell(1, 3, send = False)
        # self.activate_cell(4, 6, send = False)
        # self.send_all()
        #
        # Example #2:
        for i in range(self.size):
            self.activate_cell(i, i, send = False)
        #
        # END STANDARD ROUTING

        if send:
            self.send_all()

    def html_table(self):
        on_class = 'table-success'
        off_class = ''

        html = '<tr>' + '\n'
        html = html + '<th></th>' + '\n'
        for output in range(self.size):
            html = html + '<th>' + output_names[output] + '</th>' + '\n'
        html = html + '</tr>' + '\n'

        for input in range(self.size):
            html = html + '<tr>' + '\n'
            html = html + '<th>' + input_names[input] + '</th>' + '\n'
            for output in range(self.size):
                if self.matrix[input][output]:
                    status_class = on_class
                else:
                    status_class = off_class

                html = html + \
                    '<td id="' + str(input*8 + output) + '"' + \
                    'class="' + status_class + '">' + '</td>' + '\n'
            html = html + '</tr>'

        return html