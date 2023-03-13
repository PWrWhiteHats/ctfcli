import importlib

from ctfcli.utils.plugins import get_plugin_names


def init_plugins(commands):
    """
    Searches for the load function in modules in the ctfcli/plugins folder.
    This function is called with the current commands as a parameter.
    This allows ctfcli plugins to modify ctfcli's behavior.

    :param commands: A ctfcli commands
    :return:
    """

    for plugin in get_plugin_names():
        module = "." + plugin
        module = importlib.import_module(module, package="CTFd.plugins")
        module.load(commands)
        print(" * Loaded module, %s" % module)
