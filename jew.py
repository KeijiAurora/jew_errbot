# This is a skeleton for Err plugins, use this to get started quickly.

from errbot import BotPlugin, botcmd
from errbot.builtins.webserver import webhook


class jew(BotPlugin):
	"""A annoy Jack Heisenburg plugin  for err bot"""


	
	# Passing split_args_with=None will cause arguments to be split on any kind
	# of whitespace, just like Python's split() does
	@botcmd(split_args_with=None)
	def jew(self, mess, args):
		
		return "Jack Heisenburg someone is looking for you"
