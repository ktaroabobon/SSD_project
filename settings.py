import configparser
import pathlib

config = configparser.ConfigParser()
config.read("settings.ini", encoding="utf-8")

weight_file = config['torch']['weight']

confidence_level = float(config['predict']['confidence_level'])

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
