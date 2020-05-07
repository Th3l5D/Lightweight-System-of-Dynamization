#!usr/bin/python3


import time

class plugin2(object):

	def __init__(self, plugin_instance):
		self.recipes = {
		'anotherPlugin' : {
			'recipe' : self.forPrintAndProfit,
			'ingredients' : "prod",
			},
		'bestPluginEver' : {
			'recipe' : self.PrintWars,
			'ingredients' : "prod",
			}
		}
		self.plugin_instance = plugin_instance


	def forPrintAndProfit(self, asset):
		print('NCv6 in 2020')


	def PrintWars(self, asset):
		time.sleep(5)
		print('NCv6 For The Win')
