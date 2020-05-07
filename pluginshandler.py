#!usr/bin/python3

import importlib
import os
import sys
import traceback
import threading
import queue
import time


class PluginsHandler(object):
    """docstring for Plugins"""
    def __init__(self):
        super(PluginsHandler, self).__init__()
        self.recipes = {}
        self.running_plugins = {}


    def loadPlugins(self, reload_plugins = False):
        """ Creates an instance of every module.
        Modules are loaded dinamically in order to be at most generic as possible """
        blacklist = ['__init__.py', '__init.py', 'plugins.py', '__pycache__']

        path = os.path.abspath(__file__)[0:__file__.rfind(os.sep, 1)]+os.sep+'plugins'+os.sep
        for root, dirs, files in os.walk(path):
            for name in dirs:
                if name not in blacklist:
                    module_import = '.'.join(('plugins', name, 'main'))
                    instance = getattr(importlib.import_module(module_import), name)(self)
                    try:
                        for recipe_name, data_type in instance.recipes.items():
                            if recipe_name not in self.recipes.keys():
                                self.recipes[recipe_name] = None
                            self.recipes[recipe_name] = data_type
                    except Exception as e:
                        print(e)
                        pass

        tl = threading.Thread(target=self.checkRunningPlugins, args=(self.running_plugins,))
        tl.daemon = True
        tl.start()
        return self.recipes

    def reloadPlugins(self):
        """ I'm pretty sure it doesn't work """
        for action in self.recipes:
            del action
        self.recipes = {}
        to_delete = []
        for mod in sys.modules.keys():
            if 'plugins' in mod:
                to_delete.append(mod)
        for mod in to_delete:
            del sys.modules[mod]
        return self.loadPlugins(True)

    def launchPluginAction(self, plugin_name, extra_data=None):
        if plugin_name in self.recipes:
            try:
                if self.recipes[plugin_name]['ingredients'] == "prod": # this is just for PoC purpose. In real code it is really useful
                    print('Executing Plugin '+plugin_name)
                    thread = threading.Thread(target=self.recipes[plugin_name]['recipe'], args=(extra_data,))
                    thread.start()
                    self.running_plugins[plugin_name+'@'+str(time.time())] = thread
                else:
                    print('Plugin '+plugin_name+' cannot be launch. Wrongs ingredients. Here are the needed ones:')
                    print(self.recipes[plugin_name]['ingredients'])
            except Exception as e:
                traceback.print_exc()


    def checkRunningPlugins(self, queue):
        """ private method."""
        while 1:
            time.sleep(1)
            for name, thread in list(queue.items()):
                plugin = name.split('@')[0]
                if not thread.is_alive():
                    print(name+' task is over')
                    del queue[name]
                else:
                    print(name+' is still running') # for PoC purpose


    def executeNextPlugin(self, queue):
        """ private method. will be used to keep a list of plugins to execute one after another if needed. Not implemented """
        pass