class SQLiContext:
	"""
	This module defines the mitigation logic encapsulated by the InbandSelection interface class and dynamically 
	implemented by concrete UpdateBased and ErrorBased secure mitigation strategies to mitigate SQLi attacks.
	"""

	def __init__(self, secure_strategy) -> None:
		self.secure_strategy = secure_strategy

	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
		
	def delegate_update_strategy(self, injected_input: str):
		return self.secure_strategy.update(injected_input)

	def delegate_error_strategy(self, injected_input: str):
		return self.secure_strategy.error(injected_input)