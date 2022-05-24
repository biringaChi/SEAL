import sys
sys.path.append(".")
from src.SensitiveZone.college import DBManager

class SecureInbandSelection:
	"""
	Defines a collection of “secure algorithms” implemented by concrete strategies
	"""

	def update(self, payload: str) -> None:
		pass

	def error(self, payload: str) -> None:
		pass

class UpdateBased(SecureInbandSelection):
	"""
	This modules validates input for SQLI injection 
	"""
	def update(self, payload: str) -> None:
		return DBManager().has_entergrades_secure(payload)
	
	def error(self, payload: str) -> None:
		pass

class ErrorBased(SecureInbandSelection):
	"""
	This module validates input for Code injection
	"""
	def update(self, injected_input: str) -> None:
		pass
	
	def error(self, payload: str) -> None:
		return DBManager().has_entergrades_secure(payload)
