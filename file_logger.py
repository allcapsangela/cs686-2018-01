from logger import logger

class file_logger(logger):

	"""
	Constructor
	"""
	def __init__(self, log_level, file_name = "file_log.txt"):		
		self.log_level = log_level
		self.file_name = file_name



	"""
	log
	Logs the message if log_level is less than or equal to
	the class' threshold. (In this case: prints to file.)
	"""
	def log(self, log_level, message):
		with open(self.file_name, "a+") as file:
			if log_level >= self.log_level:
				file.write(str(log_level) + ": " + message + "\n")				

