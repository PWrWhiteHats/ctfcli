import glob
import os

from ctfcli import __name__ as pkg_name


def get_plugin_dir():
    plugins_path = os.path.join(get_data_dir(), "plugins")
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)
    return os.path.join(plugins_path)


def get_plugin_names():
    modules = sorted(glob.glob(get_plugin_dir() + "/*"))
    blacklist = {"__pycache__", "__init__.py"}
    plugins = []
    for module in modules:
        module_name = os.path.basename(module)
        if os.path.isdir(module) and module_name not in blacklist:
            plugins.append(module_name)
    return plugins


def get_data_dir():
    # Original used user's data directory
    # return appdirs.user_data_dir(appname=pkg_name)
    curr_file_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.abspath(os.path.join(curr_file_dir, os.pardir))
