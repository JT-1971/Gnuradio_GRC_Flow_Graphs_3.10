"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, hseconds = 0, seconds = 0, minutes = 0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Sonoda Umi',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_in(pmt.intern('hseconds'))
        self.message_port_register_out(pmt.intern('Sonoda_Umi'))
        self.set_msg_handler(pmt.intern('hseconds'),self.check)
        self.hseconds = hseconds
        self.seconds = seconds
        self.minutes = minutes
        
        
    def work(self, input_items, output_items):
        None
    def check(self, msg):
        hseconds = self.hseconds
        seconds = self.seconds
        minutes = self.minutes
        if minutes == 0 and seconds == 23 and hseconds == 30:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 0 and seconds == 36 and hseconds == 9:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 0 and seconds == 42 and hseconds == 7:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 0 and seconds == 51 and hseconds == 30:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 0 and seconds == 54 and hseconds == 59:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 1 and seconds == 1 and hseconds == 16:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 1 and seconds == 21 and hseconds == 72:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 1 and seconds == 23 and hseconds == 86:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 1 and seconds == 24 and hseconds == 18:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 1 and seconds == 25 and hseconds == 93:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 1 and seconds == 27 and hseconds == 11:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 1 and seconds == 27 and hseconds ==97:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 1 and seconds == 46 and hseconds == 32:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 1 and seconds == 49 and hseconds == 64:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 1 and seconds == 52 and hseconds == 63:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 1 and seconds == 55 and hseconds == 64:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 1 and seconds == 58 and hseconds == 93:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 2 and seconds == 1 and hseconds == 75:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 2 and seconds == 4 and hseconds == 98:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 2 and seconds == 11 and hseconds == 62:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 2 and seconds == 33 and hseconds == 24:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 2 and seconds == 34 and hseconds == 80:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 2 and seconds == 35 and hseconds == 38:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 2 and seconds == 37 and hseconds == 29:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 2 and seconds == 45 and hseconds == 40:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 2 and seconds == 54 and hseconds == 86: # 间奏
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 3 and seconds == 10 and hseconds == 71:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 3 and seconds == 13 and hseconds == 57:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 3 and seconds == 17 and hseconds == 7:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 3 and seconds == 23 and hseconds == 31:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 3 and seconds == 42 and hseconds == 34:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 3 and seconds == 44 and hseconds == 53: # tooi
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 3 and seconds == 45 and hseconds == 13: # yume no[Honoka]
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 3 and seconds == 46 and hseconds == 97: # dakedo
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
        if minutes == 3 and seconds == 47 and hseconds == 68:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(0)))
        if minutes == 3 and seconds == 49 and hseconds == 7:
            self.message_port_pub(pmt.intern('Sonoda_Umi'),pmt.cons(pmt.string_to_symbol("Sonoda_Umi"), pmt.from_long(1)))
