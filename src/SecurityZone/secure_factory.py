import sys
sys.path.append(".")
from src.SecurityZone.secure_strategy import UpdateBased, ErrorBased

class SecureFactory:
	"""
	This module defines an interface for creating secure strategies implemented using the 
	UpdateFactory and ErrorFactory classes to create concrete UPDATE and ERROR security strategies.
	"""
	def __init__(self) -> None:
		super().__init__()
		
	def retrieve_strategy(self):
		pass

class UpdateFactory(SecureFactory):
	def retrieve_strategy(self):
		print("Retrieving UPDATE factory")
		return UpdateBased()

class ErrorFactory(SecureFactory):
	def retrieve_strategy(self):
		print("Retrieving ERROR factory")
		return ErrorBased()
	
class FactoryHandler:
	def handle(self, Factory):
		return Factory.retrieve_strategy(self)