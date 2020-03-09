patchbay_matrix
===============

Driver for Opcode Studio 128X MIDI Patchbay, including web interface and shell.
Developed by Fabian Hummel for Klangwerkstatt Graz (March 2020).
Large parts of 'patchbay_matrix/patchbay_driver' based on the reverse
engineering work done by Maxwell Pray (@synthead).

Install
-------

    pip install -r requirements.txt

Configure
---------

- You need a *USB <--> RS232* cable with the appropriate drivers installed.
- Make sure the correct serial port (e.g. *'/dev/usb.ttyserial'*) is set in *'shell.py'* and *'patchbay_matrix/__init__.py'*.

Web Server
----------

### Run

    python server.py

### Use

- Navigate to *http://localhost:5000* in your browser
- Click connect
- Play around

*Note:* If you disconnect the device or serial cable while the software thinks it's connected you may encounted some strange behaviour. Clicking *Connect* twice should solve the problem in most cases, but you may have to restart the Opcode Studio 128X and/or the software.

### Customize

You can set custom channel names for your hardware configuration in *'patchbay_matrix/channel_names.py'*.
Additionally, you can set a standard routing configuration in  *'patchbay_matrix/RoutingMatrix.py'*.
This works independently of the routing patches stored on the Opcode Studio 128X.

Python Shell
------------
### Run

    python shell.py

### MIDI Routing

Enable MIDI routing from input a (1-8) to output b (1-8):

    x.route(a, b)
    
Disable MIDI routing from input a to output b:

    x.route(a, b, enable = False)

### Patch Selection/Storage:

Select patch number n (1-8):

    x.select_patch(n)
    
Store current configuration in patch number n (1-8):

    x.store_patch(n)
    
More commands are available but not implemented. See
*'patchbay_matrix/patchbay_driver/hexcodes.py'* for more info.