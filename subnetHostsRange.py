#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
########################
##  subnetHostsRange  ##
########################

Extract host ranges from a list of subnets

### Source code info:
Code formatting by autopep8 --max-line-length=150
"""
from datetime import timedelta
from timeit import default_timer as timer
from pathlib import Path
import argparse  # cli interface
import logging
import ipaddress

__author__ = 'cyb3rw0lf'
__credits__ = ['cyb3rw0lf']
__appName__ = 'subnetHostsRange'
__license__ = 'MIT'
__version__ = 'v1.0.0'
__appVers__ = '%s v%s' % (__appName__, __version__)
__status__ = 'Production'
__maintainer__ = 'cyb3rw0lf'
__homepage__ = 'https://github.com/cyb3rw0lf/'
__email__ = 'w0lf.code@pm.me'
__issues__ = 'https://github.com/cyb3rw0lf/subnetHostsRange/issues'
__usage__ = ('Extract host ranges from a list of subnets')


def main():
    # START CLI UI
    parser = argparse.ArgumentParser(description=__usage__)
    parser.add_argument('-v', '--version', action='version', version=__appVers__)
    parser.add_argument('file', type=str, help='Input file with Network/Subnet in each line')
    parser.add_argument('-o', type=str, help='Output file name [default = same as input]', metavar='output_file')
    parser.add_argument('-d', '--debug', help='enable logging debug', default=False, action="store_true")
    args = parser.parse_args()
    # END CLI UI
    # Logging to STDOUT
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    if not args.debug:
        logging.disable(logging.DEBUG)
    logging.info('Session Started')
    # Do something here

    if args.o is None:
        # Set default output file name as input
        outFile = f'{Path(args.file).stem}_ranges.txt'
    else:
        outFile = args.o

    # Open the input file as text
    with open(args.file, encoding='utf8') as f:
        text = f.read().splitlines()

    with open(outFile, 'w') as out:
        for line in text:
            logging.debug(f'Network: {line}')
            Subnet = ipaddress.ip_interface(line).network
            fourthHost = list(Subnet.hosts())[3]
            lastHost = list(Subnet.hosts())[-1]
            hostsRange = f'{fourthHost} - {lastHost}\n'
            logging.debug(f'Ranges: {hostsRange}')
            out.write(hostsRange)

    logging.info(f'Created output file: {outFile}')

    logging.info('Session Finished')
    end_time = timer()
    logging.info(f'Duration: {(timedelta(seconds=end_time-start_time))}')


if __name__ == '__main__':
    start_time = timer()
    main()
