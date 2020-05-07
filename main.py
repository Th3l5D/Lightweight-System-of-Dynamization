#!/use/bin/python3

import pluginshandler

# It's only a PoC, so these instruction are quite useless.
# But the point of this script is just to show how to use plugins



commands = ['plugin1', 'plugin1ButAnother', 'anotherPlugin', 'bestPluginEver']


plugins = pluginshandler.PluginsHandler()
plugins.loadPlugins()

while 1:
	cmd = input('>>').strip()
	if cmd in commands:
		plugins.launchPluginAction(cmd)
	else:
		print('Wrong command')