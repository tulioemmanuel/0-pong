import json
import os
import sys
import logging


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuration(metaclass=SingletonMeta):
    CONFIGURATION_JSON_FILE_NAME = "config.json"
    SRC_FOLDER_NAME = "src"
    ASSETS_FOLDER_NAME = "assets"

    settings = {}

    def __init__(self):
        # logging.info("Loading Configuration..")
        # logging.info("Asset Dir path: %s".format(assets_dir_path))
        # print("Asset Dir path: %s".format(assets_dir_path))

        # assets_dir_path = os.path.join(
        #     os.path.join("")
        #     if sys.platform == "emscripten"
        #     else os.path.join(os.getcwd())
        # )

        # with open(Configuration.CONFIGURATION_JSON_FILE_NAME) as config_file:
        #     config_json = json.load(config_file)
        #     for key in config_json:
        #         Configuration.settings[key] = config_json[key]
        pass
