import numpy
import pandas as pd
import yaml
import re
import can
import sys
import os.path
from os import path
from amp_can_raw.parsers import dbc_parser
from amp_can_raw.interaction.codec import NetworkCodec

def make_value_series_for_signal(matched_signal, commands, data_rate):
    value_series = [matched_signal]
    end_value = 0.0
    end_time = -data_rate
    for command in commands:
        for index, parameters in command.items():
            start_time = end_time
            start_value = end_value
            end_value = parameters['value']
            end_time = parameters['endTime']

            if end_time % data_rate != 0:
                print("end_time {et} is not a multiple of data_rate {dr}! Exiting.".format(et=end_time,
                    dr=data_rate))
                sys.exit(1)

            op = parameters['op']
            for cur_time in numpy.arange(start_time+data_rate, end_time+data_rate, data_rate):
                if op == 'hold':
                    value_series.append(end_value)
                else:
                    time_length = end_time - start_time
                    value_diff = end_value - start_value
                    slope = value_diff / time_length
                    time_since_start = cur_time - start_time
                    value = round(start_value + time_since_start * slope, 3)
                    value_series.append(value)
    return value_series

# Find all signals specified by yaml file.
# Create value-series for those signals (again specified by yaml file)
# Make dataframe from all that info.
def make_dataframe(instructions, signal_names, data_rate):
    assert(type(instructions) == dict)

    for signal, commands in instructions.items():
        columns = ['Signals']
        final_command=commands[-1]
        end_time = 0.0
        for index, parameters in final_command.items():
            if parameters['endTime'] > end_time:
                end_time = parameters['endTime']
        start_time = -data_rate
        for cur_time in numpy.arange(start_time+data_rate, end_time+data_rate, data_rate):
            columns.append(cur_time)
    df = pd.DataFrame(columns=columns)

    for regex, commands in instructions.items():
        # Find all signals specified by yaml file.
        r = re.compile(regex)
        matched_signals = list(filter(r.match, signal_names))

        for matched_signal in matched_signals:
            # Create value-series for those signals.
            if matched_signal in list(df.index):
                continue
            value_series = make_value_series_for_signal(matched_signal, commands, data_rate)


            # Add the value series as a row to the df.
            values_to_add = {}
            i = 0
            for column in columns:
                values_to_add[column] = value_series[i]
                i += 1
            row_to_add = pd.Series(values_to_add, name=matched_signal)
            df = df.append(row_to_add)

    return df

def make_signal_names_list(network):
    bms_node = network.nodes['BMS']
    msg_names = []
    for msg in bms_node._rx_messages:
        msg_names.append(msg.name)
    signal_names = []
    for signal in bms_node.rx_signals:
        signal_names.append(signal.name)
    return signal_names

# Find all signals specified by yaml file.
# Create value-series for those signals (again specified by yaml file)
# Make dataframe from all that info.
# print dataframe to csv.
def generate_csv_from_yaml(codec, network, yaml_file, csv_file):
    assert(type(codec) == NetworkCodec)
    #  assert(type(network) == Network)
    assert(type(yaml_file) == str)
    assert(type(csv_file) == str)

    if not path.exists(yaml_file):
        click.echo("Cannot find file at path {f}".format(f=yaml_file))
        sys.exit(1)

    signal_names = make_signal_names_list(network)

    instructions_yaml = open(yaml_file, 'r')
    instructions = yaml.load(instructions_yaml, Loader=yaml.SafeLoader)

    if 'dataRate' in instructions:
        data_rate = instructions['dataRate']
        instructions.pop('dataRate', None)
    #  else:
        # find data_rate in dbc.

    # Find all signals specified by yaml file.
    # Create value-series for those signals (again specified by yaml file)
    # Make dataframe from all that info.
    df = make_dataframe(instructions, signal_names, data_rate)

    # print dataframe to csv.
    print("Generated this dataframe from {y} and printing it to {c}:\n{df}".format(y=yaml_file, df=df.to_string(index=False), c=csv_file))
    df.to_csv(csv_file, index = False)
