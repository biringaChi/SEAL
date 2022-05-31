import sys
sys.path.append(".")
from SecurityZone.inband_selection import UpdateBased, ErrorBased

class SecureFactory:
	"""
	This module defines an interface for creating secure strategies implemented using the 
	UpdateFactory and ErrorFactory classes to create concrete UPDATE and ERROR security strategies.
	"""
	def __init__(self) -> None:
		super().__init__()

	def __str__(self) -> str:
		return self.__class__.__name__
		
	def __repr__(self) -> str:
		return self.__str__()
		
	def retrieve_strategy(self):
		pass

class UpdateFactory(SecureFactory):
	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()

	def retrieve_strategy(self):
		print("Retrieving UPDATE factory")
		return UpdateBased()

class ErrorFactory(SecureFactory):
	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()

	def retrieve_strategy(self):
		print("Retrieving ERROR factory")
		return ErrorBased()
	
class FactoryHandler:
	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
		
	def handle(self, Factory):
		return Factory.retrieve_strategy(self)