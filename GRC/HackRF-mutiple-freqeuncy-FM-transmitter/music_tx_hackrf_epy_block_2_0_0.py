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
            name='Minami Kotori',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_in(pmt.intern('hseconds'))
        self.message_port_register_out(pmt.intern('Minami_Kotori'))
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
        if minutes == 0 and seconds == 36 and hseconds == 9:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 0 and seconds == 48 and hseconds == 60:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 0 and seconds == 51 and hseconds == 34:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 1 and seconds == 1 and hseconds == 16:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 1 and seconds == 21 and hseconds == 72:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 1 and seconds == 22 and hseconds == 87:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 1 and seconds == 23 and hseconds == 86:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 1 and seconds == 24 and hseconds == 99:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 1 and seconds == 25 and hseconds == 93:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 1 and seconds == 27 and hseconds == 97:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 1 and seconds == 49 and hseconds == 64:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 1 and seconds == 55 and hseconds == 64:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 2 and seconds == 1 and hseconds == 75:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 2 and seconds == 11 and hseconds == 62:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 2 and seconds == 32 and hseconds ==7:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 2 and seconds == 34 and hseconds == 35:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 2 and seconds == 34 and hseconds == 80:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 2 and seconds == 36 and hseconds == 30:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 2 and seconds == 37 and hseconds == 29:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 2 and seconds == 38 and hseconds == 61:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 2 and seconds == 45 and hseconds == 40: 
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 2 and seconds == 54 and hseconds == 86: # 间奏
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 3 and seconds == 13 and hseconds == 57:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 3 and seconds == 23 and hseconds == 31:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 3 and seconds == 42 and hseconds == 34:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 3 and seconds == 43 and hseconds == 63:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 3 and seconds == 44 and hseconds == 53: # tooi[Umi]
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 3 and seconds == 45 and hseconds == 57: # kakera
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
        if minutes == 3 and seconds == 46 and hseconds == 97: # Dakedo
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(0)))
        if minutes == 3 and seconds == 49 and hseconds == 7:
            self.message_port_pub(pmt.intern('Minami_Kotori'),pmt.cons(pmt.string_to_symbol("Minami_Kotori"), pmt.from_long(1)))
