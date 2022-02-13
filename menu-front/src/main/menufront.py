#--- library -----------------------------------------------------------------------#
import argparse as arg
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
my_parser.add_argument('URL',
                        metavar='url',
                        type=str,
                        help='the path to list')


"""
retrieve the different arguments in a variable
"""
args = my_parser.parse_args()
url = args.URL

listmenus(url)