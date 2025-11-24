#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ww
# Author: ee
# Description: rr
# GNU Radio version: v3.11.0.0git-991-g721e477c

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
import osmosdr
import time
import threading
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation




class fm_helloworld(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ww", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ww")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "fm_helloworld")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.quadrature = quadrature = 250e3
        self.cutoff = cutoff = 100e3
        self.audio_rate = audio_rate = 48e3

        ##################################################
        # Blocks
        ##################################################

        self.wbfm_analog_receiver = analog.wfm_rcv(
        	quad_rate=quadrature,
        	audio_decimation=1,
        	deemph_tau=(75e-6),
        )
        self.volume_multiplier = blocks.multiply_const_ff(.5)
        self.resampler_toward_sink_rate = filter.rational_resampler_fff(
                interpolation=(int(audio_rate/1e3)),
                decimation=(int(quadrature/1e3)),
                taps=[],
                fractional_bw=0)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'hackrf=0'
        )
        self.osmosdr_source_0.set_time_source('external', 0)
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(435.1e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(32, 0)
        self.osmosdr_source_0.set_bb_gain(32, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.fm_low_pass_filter = filter.fir_filter_ccf(
            (int(samp_rate/quadrature)),
            firdes.low_pass(
                1,
                samp_rate,
                cutoff,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.fm_low_pass_filter, 0), (self.wbfm_analog_receiver, 0))
        self.connect((self.osmosdr_source_0, 0), (self.fm_low_pass_filter, 0))
        self.connect((self.resampler_toward_sink_rate, 0), (self.volume_multiplier, 0))
        self.connect((self.volume_multiplier, 0), (self.audio_sink_0, 0))
        self.connect((self.wbfm_analog_receiver, 0), (self.resampler_toward_sink_rate, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "fm_helloworld")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fm_low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, 10000, window.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.fm_low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, 10000, window.WIN_HAMMING, 6.76))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate




def main(top_block_cls=fm_helloworld, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

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
