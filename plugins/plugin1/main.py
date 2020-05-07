#!usr/bin/python3


class plugin1(object):

	def __init__(self, plugin_instance):
		self.recipes = {
		'plugin1' : {
			'recipe' : self.thisIsPrinta,
			'ingredients' : "prod",
			},
		'plugin1ButAnother' : {
			'recipe' : self.forThePrint,
			'ingredients' : "debug",
			}
		}
		self.plugin_instance = plugin_instance


	def thisIsPrinta(self, asset):
		print('Th3_l5D is da best')


	def forThePrint(self, asset):
		print('Th3_l5D is still da best')
