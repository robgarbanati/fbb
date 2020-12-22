import can
import threading
import pandas as pd
import socket
import sys
import struct
import time
import platform
import os.path
import click
from os import path
from datetime import datetime
from datetime import timedelta

from amp_can_raw.parsers import dbc_parser
from amp_can_raw.interaction.codec import NetworkCodec

def find_msg(network, signal_name):
    list_of_msgs = []

    bms_node = network.nodes['BMS']
    for message in bms_node._rx_messages:
        #  print("name={n}, msg={m}: s={s}".format(n=message.name, m=message, s=message.signals))
        for signal in message.signals:
            if(signal_name == signal.name):
                #  print(signal.name)
                list_of_msgs.append(message)
    return list_of_msgs

def send_can_msgs(bus, signal_values_df, codec, msgs, begin, timestamp_index):
    assert(type(signal_values_df) == pd.DataFrame)
    assert(type(timestamp_index) == int)

    timestamp = signal_values_df.columns[timestamp_index]
    run_at = begin + timedelta(seconds=float(timestamp))
    print("timestamp={ts}".format(ts=timestamp))
    print(signal_values_df[timestamp])
    # TODO move this to the bottom of the function.
    now = datetime.now()
    delay = (run_at - now).total_seconds()
    if timestamp_index+1 < len(signal_values_df.columns):
        threading.Timer(delay, send_can_msgs, [bus, signal_values_df, codec, msgs, begin, timestamp_index+1]).start()

    can_msgs = codec.pack_messages_at_time(msgs, signal_values_df, timestamp)

    if bus == 0:
        fmt = "<IB3x8s"
        sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        interface = "can0"
        try:
            sock.bind((interface,))
        except OSError:
            sys.stderr.write("Could not bind to interface '%s'\n" % interface)
            # do something about the error...

    for can_msg in can_msgs:
        if bus == 0:
            can_pkt = struct.pack(fmt, can_msg.arbitration_id, len(can_msg.data), can_msg.data)
            print(can_pkt)
            sock.send(can_pkt)
        else:
            print(can_msg)
            bus.send(can_msg)
    print("")

def find_msgs_from_signals_in_df(network, signal_values_df):
    signal_names = signal_values_df.index
    msgs = []

    for signal_name in signal_names:
        found_messages = find_msg(network, signal_name)
        msgs = list(set(msgs).union(found_messages))
    return msgs


def gen_can_from_csv(codec, network, csv_file):
    assert(type(codec) == NetworkCodec)
    #  assert(type(network) == Network)
    assert(type(csv_file) == str)

    if not path.exists(csv_file):
        click.echo("Cannot find file at path {f}".format(f=csv_file))
        sys.exit(1)

    signal_values_df = pd.read_csv(csv_file, index_col=0)
    msgs = find_msgs_from_signals_in_df(network, signal_values_df)

    if platform.system() == 'Linux':
        bus = 0
    else:
        bus = can.interface.Bus()

    # Initialize variables for scheduling can messages with threading.Timer
    timestamp_index = 0
    timestamp = signal_values_df.columns[timestamp_index]
    begin = datetime.now()
    run_at = begin + timedelta(seconds=float(timestamp))
    now = datetime.now()
    delay = (run_at - now).total_seconds()

    if timestamp_index+1 < len(signal_values_df.columns):
        threading.Timer(delay, send_can_msgs, [bus, signal_values_df, codec, msgs, begin, timestamp_index+1]).start()

