from logger import logger
class stdout_logger(logger):


	"""
    Constructor
    """
	def __init__(self, log_level):
		self.log_level = log_level

	"""
	log
	Logs the message if log_level is less than or equal to
	the class' threshold. (In this case: prints to console.)
	"""
	def log(self, log_level, message):
		if log_level >= self.log_level:
			print str(log_level) + ": " + message