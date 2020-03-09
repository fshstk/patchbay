################################################################################
# patchbay_matrix
# Python web interface for Opcode Studio 128X
#
# (c) Fabian Hummel 2020
# License: GNU GPL v3
#
# Uses flask to display a (8x8) routing matrix as a web interface.
# Cells are clickable which automatically updates their status.
# Clear all and a pre-defined standard program are also available.
################################################################################

from flask import Flask, render_template, request

from .RoutingMatrix import RoutingMatrix
from .patchbay_driver import OpcodeStudio128X

app = Flask(__name__)

serial_port = '/dev/tty.usbserial'
patchbay = OpcodeStudio128X(serial_port, init = False)
matrix = RoutingMatrix(patchbay)
#matrix = RoutingMatrix(None)
is_connected = False

@app.route('/')
def routing():
    return render_template('routing.html', table = matrix.html_table(), is_connected = is_connected)

@app.route('/toggle', methods = ['GET', 'POST'])
def cell_clicked():
    id = int(request.form['id'])
    matrix.toggle_cell_by_id(id, send = True)
    return matrix.html_table()

@app.route('/clear', methods = ['GET', 'POST'])
def clear_clicked():
    matrix.clear_all(send = True)
    return matrix.html_table()

@app.route('/standard', methods = ['GET', 'POST'])
def standard_routing_clicked():
    matrix.standard_routing(send = True)
    return matrix.html_table()

@app.route('/connect', methods = ['GET', 'POST'])
def connect_clicked():
    global is_connected

    try:
        if is_connected:
            patchbay.deinit()
        else:
            patchbay.init()
            matrix.send_all()
        is_connected = not is_connected
    except:
        is_connected = False

    return "1" if is_connected else "0"

if __name__ == '__main__':
    app.run(debug = True)