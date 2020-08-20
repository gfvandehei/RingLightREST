import configparser
import sys

config_file_path = sys.argv[1]

config = configparser.ConfigParser()
config.read(config_file_path)