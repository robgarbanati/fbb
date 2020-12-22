import click
import csv_generator
import csv_emulator
import sys
import os.path
from os import path
from amp_can_raw.parsers import dbc_parser
from amp_can_raw.interaction.codec import NetworkCodec

@click.command()
@click.option('--generate-csv', '-g', is_flag=True, help='Set this flag to generate a csv.')
@click.option('--emulate-csv', '-e', is_flag=True, help='Set this flag to emulate a csv.')
@click.option('--dbc-file', '-d', type=str, default='vho_emulator.dbc', help='Specify path to dbc file.')
@click.option('--yaml-file', '-y', type=str, default='voltages01module01.yaml', help='Specify path to yaml file.')
@click.option('--csv-file', '-c', type=str, default='battery_emulator.csv', help='Specify path to csv file.')
def cli(generate_csv, emulate_csv, yaml_file, csv_file, dbc_file):

    if not path.exists(dbc_file):
        click.echo("Cannot find file at path {f}".format(f=dbc_file))
        sys.exit(1)

    with open(dbc_file, 'r') as dbc:
        network = dbc_parser.get_dbc_parser().parse(dbc.read())

    codec = NetworkCodec(network)

    if(generate_csv):
        csv_generator.generate_csv_from_yaml(codec, network, yaml_file, csv_file)

    if(emulate_csv):
        csv_emulator.gen_can_from_csv(codec, network, csv_file)

    if not generate_csv and not emulate_csv:
        click.echo("Neither -g nor -e flags set; nothing to do!")

if __name__ == '__main__':
    cli()

