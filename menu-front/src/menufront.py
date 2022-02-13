#--- library -----------------------------------------------------------------------#
import argparse as arg
from asyncio import constants
import requests
from services.delete import *
from services.list import *
#-----------------------------------------------------------------------------------#

"""
create the command line parser with its name and description
"""
my_parser = arg.ArgumentParser(prog="menufront", description='Request the menuserver API')


""""
define what will be the command line arguments and options
"""
my_parser.add_argument('-URL',
                        metavar='url',
                        type=str,
                        help='the path to list')

my_parser.add_argument('-list',
                        action='store_true',
                        help='list all the menu')

my_parser.add_argument('-delete',
                    help='delete a menu withe a given id',
                    type=str,
                    nargs=1
                    )

"""
retrieve the different arguments in a variable
"""
args = my_parser.parse_args()

with open('services/constants.txt') as files:
    BASE_URL = files.read()
if (args.URL):
    with open('services/constants.txt', mode='w') as files:
        files.write(args.URL)
elif (args.delete):
    delete(BASE_URL,args.delete[0])
elif(args.list):
    listmenus(BASE_URL)
