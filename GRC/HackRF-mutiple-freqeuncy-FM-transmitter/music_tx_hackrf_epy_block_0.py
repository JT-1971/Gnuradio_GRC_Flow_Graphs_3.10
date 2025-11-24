"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt
import time


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Timer',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_out(pmt.intern('minute'))
        self.message_port_register_out(pmt.intern('second'))
        self.message_port_register_out(pmt.intern('hsecond'))
    def work(self,input_items, output_items):
        start = time.time()
        while (True):
            elap = time.time() - start
            minutes = int (elap / 60)
            seconds = int (elap - minutes * 60)
            hseconds = int((elap - minutes*60.0 - seconds) *100)
            seconds_message = pmt.from_long (seconds)
            minutes_message = pmt.from_long (minutes)
            hseconds_message = pmt.from_long (hseconds)
            self.message_port_pub(pmt.intern('hsecond'), pmt.cons(pmt.string_to_symbol("hseconds"), hseconds_message))
            self.message_port_pub(pmt.intern('second'),pmt.cons(pmt.string_to_symbol("seconds"), seconds_message))
            self.message_port_pub(pmt.intern('minute'), pmt.cons(pmt.string_to_symbol("minutes"), minutes_message))
            time.sleep(0.001)
            
