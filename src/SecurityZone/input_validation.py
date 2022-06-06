from typing import Union

class InputValidation:
	"""
	This module performs a light input validation from
	injected payload from the Injection Zone
	"""

	def __init__(self) -> None:
		pass

	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()
	
	def validate(self, payload: str) -> Union[str, bool]: 
		return payload if isinstance(payload, str) else False