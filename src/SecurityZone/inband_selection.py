import sys
sys.path.append(".")
from SensitiveZone.sensitive_zone import DBManager

class SecureInbandSelection:
	"""
	This module defines the dynamic selection of implemented secure mitigation 
	algorithms. It processes requests from the SQLiContext and passes that information 
	to the derived concrete classes base on a detected threat.
	"""

	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()

	def update(self, payload: str):
		pass

	def error(self, payload: str):
		pass

class UpdateBased(SecureInbandSelection):
	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
		
	def update(self, payload: str):
		return DBManager().has_entergrades_secure(payload)
	
	def error(self, payload: str):
		pass

class ErrorBased(SecureInbandSelection):
	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
		
	def update(self, injected_input: str):
		pass
	
	def error(self, payload: str):
		return DBManager().has_entergrades_secure1(payload)