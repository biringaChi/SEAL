import sys
sys.path.append(".")
from src.SecurityZone.secure_strategy import UpdateBased, ErrorBased

class SecureFactory:
	"""
	Defines the creation of security strategies implemented by Factory concrete class.
	"""
	def __init__(self) -> None:
		super().__init__()
		
	def retrieve_strategy(self):
		pass

class UpdateFactory(SecureFactory):
	"""
	Implementing factory class for ...
	"""
	def retrieve_strategy(self):
		print("Retrieving UPDATE factory")
		return UpdateBased()

class ErrorFactory(SecureFactory):
	"""
	Implementing factory class for ....
	"""
	def retrieve_strategy(self):
		print("Retrieving ERROR factory")
		return ErrorBased()
	
class FactoryHandler:
	def handle(self, Factory) -> None:
		return Factory.retrieve_strategy(self)