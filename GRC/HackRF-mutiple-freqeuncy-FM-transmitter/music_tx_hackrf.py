#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Music Tx Hackrf
# GNU Radio version: v3.11.0.0git-991-g721e477c

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
import math
from gnuradio import filter
from gnuradio.filter import firdes
import music_tx_hackrf_epy_block_0 as epy_block_0  # embedded python block
import music_tx_hackrf_epy_block_2 as epy_block_2  # embedded python block
import music_tx_hackrf_epy_block_2_0 as epy_block_2_0  # embedded python block
import music_tx_hackrf_epy_block_2_0_0 as epy_block_2_0_0  # embedded python block
import osmosdr
import time
import sip
import threading
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation




class music_tx_hackrf(gr.top_block, Qt.QWidget):

    def __init__(self, freq=146e6, ppm=0, samp_rate=44.1e3):
        gr.top_block.__init__(self, "Music Tx Hackrf", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Music Tx Hackrf")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "music_tx_hackrf")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.ppm = ppm
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.seconds = seconds = 0
        self.minutes = minutes = 0
        self.hseconds = hseconds = 0
        self.Sonoda_Umi = Sonoda_Umi = 1
        self.Minami_Kotori = Minami_Kotori = 1
        self.Kosaka_Honoka = Kosaka_Honoka = 1

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=100,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + 'hackrf=0'
        )
        self.osmosdr_sink_0.set_sample_rate((samp_rate*100))
        self.osmosdr_sink_0.set_center_freq(146e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.epy_block_2_0_0 = epy_block_2_0_0.blk(hseconds=hseconds, seconds=seconds, minutes=minutes)
        self.epy_block_2_0 = epy_block_2_0.blk(hseconds=hseconds, seconds=seconds, minutes=minutes)
        self.epy_block_2 = epy_block_2.blk(hseconds=hseconds, seconds=seconds, minutes=minutes)
        self.epy_block_0 = epy_block_0.blk(example_param=1.0)
        self.blocks_var_to_msg_0_0_0 = blocks.var_to_msg_pair('')
        self.blocks_var_to_msg_0_0 = blocks.var_to_msg_pair('')
        self.blocks_var_to_msg_0 = blocks.var_to_msg_pair('')
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_cc(Sonoda_Umi)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(Kosaka_Honoka)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Minami_Kotori)
        self.blocks_msgpair_to_var_3_0_0 = blocks.msg_pair_to_var(self.set_Minami_Kotori)
        self.blocks_msgpair_to_var_3_0 = blocks.msg_pair_to_var(self.set_Kosaka_Honoka)
        self.blocks_msgpair_to_var_3 = blocks.msg_pair_to_var(self.set_Sonoda_Umi)
        self.blocks_msgpair_to_var_2 = blocks.msg_pair_to_var(self.set_hseconds)
        self.blocks_msgpair_to_var_1 = blocks.msg_pair_to_var(self.set_minutes)
        self.blocks_msgpair_to_var_0 = blocks.msg_pair_to_var(self.set_seconds)
        self.blocks_freqshift_cc_2 = blocks.rotator_cc(2.0*math.pi*0.0/(samp_rate*100))
        self.blocks_freqshift_cc_1 = blocks.rotator_cc(2.0*math.pi*(-1.5e6)/(samp_rate*100))
        self.blocks_freqshift_cc_0 = blocks.rotator_cc(2.0*math.pi*1e6/(samp_rate*100))
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.audio_source_0 = audio.source(44100, '', True)
        self.analog_wfm_tx_1 = analog.wfm_tx(
        	audio_rate=44100,
        	quad_rate=44100,
        	tau=(75e-6),
        	max_dev=3e3,
        	fh=(-1.0),
        )


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_var_to_msg_0, 'msgout'), (self.epy_block_2, 'hseconds'))
        self.msg_connect((self.blocks_var_to_msg_0_0, 'msgout'), (self.epy_block_2_0, 'hseconds'))
        self.msg_connect((self.blocks_var_to_msg_0_0_0, 'msgout'), (self.epy_block_2_0_0, 'hseconds'))
        self.msg_connect((self.epy_block_0, 'second'), (self.blocks_msgpair_to_var_0, 'inpair'))
        self.msg_connect((self.epy_block_0, 'minute'), (self.blocks_msgpair_to_var_1, 'inpair'))
        self.msg_connect((self.epy_block_0, 'hsecond'), (self.blocks_msgpair_to_var_2, 'inpair'))
        self.msg_connect((self.epy_block_2, 'Sonoda_Umi'), (self.blocks_msgpair_to_var_3, 'inpair'))
        self.msg_connect((self.epy_block_2_0, 'Kosaka_Honoka'), (self.blocks_msgpair_to_var_3_0, 'inpair'))
        self.msg_connect((self.epy_block_2_0_0, 'Minami_Kotori'), (self.blocks_msgpair_to_var_3_0_0, 'inpair'))
        self.connect((self.analog_wfm_tx_1, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.audio_source_0, 0), (self.analog_wfm_tx_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_freqshift_cc_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_freqshift_cc_1, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_freqshift_cc_2, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_null_source_0, 0), (self.epy_block_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_freqshift_cc_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_freqshift_cc_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_freqshift_cc_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "music_tx_hackrf")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*1e6/(self.samp_rate*100))
        self.blocks_freqshift_cc_1.set_phase_inc(2.0*math.pi*(-1.5e6)/(self.samp_rate*100))
        self.blocks_freqshift_cc_2.set_phase_inc(2.0*math.pi*0.0/(self.samp_rate*100))
        self.osmosdr_sink_0.set_sample_rate((self.samp_rate*100))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_seconds(self):
        return self.seconds

    def set_seconds(self, seconds):
        self.seconds = seconds
        self.epy_block_2.seconds = self.seconds
        self.epy_block_2_0.seconds = self.seconds
        self.epy_block_2_0_0.seconds = self.seconds

    def get_minutes(self):
        return self.minutes

    def set_minutes(self, minutes):
        self.minutes = minutes
        self.epy_block_2.minutes = self.minutes
        self.epy_block_2_0.minutes = self.minutes
        self.epy_block_2_0_0.minutes = self.minutes

    def get_hseconds(self):
        return self.hseconds

    def set_hseconds(self, hseconds):
        self.hseconds = hseconds
        self.blocks_var_to_msg_0.variable_changed(self.hseconds)
        self.blocks_var_to_msg_0_0.variable_changed(self.hseconds)
        self.blocks_var_to_msg_0_0_0.variable_changed(self.hseconds)
        self.epy_block_2.hseconds = self.hseconds
        self.epy_block_2_0.hseconds = self.hseconds
        self.epy_block_2_0_0.hseconds = self.hseconds

    def get_Sonoda_Umi(self):
        return self.Sonoda_Umi

    def set_Sonoda_Umi(self, Sonoda_Umi):
        self.Sonoda_Umi = Sonoda_Umi
        self.blocks_multiply_const_vxx_2.set_k(self.Sonoda_Umi)

    def get_Minami_Kotori(self):
        return self.Minami_Kotori

    def set_Minami_Kotori(self, Minami_Kotori):
        self.Minami_Kotori = Minami_Kotori
        self.blocks_multiply_const_vxx_0.set_k(self.Minami_Kotori)

    def get_Kosaka_Honoka(self):
        return self.Kosaka_Honoka

    def set_Kosaka_Honoka(self, Kosaka_Honoka):
        self.Kosaka_Honoka = Kosaka_Honoka
        self.blocks_multiply_const_vxx_1.set_k(self.Kosaka_Honoka)



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-f", "--freq", dest="freq", type=eng_float, default=eng_notation.num_to_str(float(146e6)),
        help="Set freq [default=%(default)r]")
    parser.add_argument(
        "-p", "--ppm", dest="ppm", type=eng_float, default=eng_notation.num_to_str(float(0)),
        help="Set ppm [default=%(default)r]")
    return parser


def main(top_block_cls=music_tx_hackrf, options=None):
    if options is None:
        options = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(freq=options.freq, ppm=options.ppm)

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
