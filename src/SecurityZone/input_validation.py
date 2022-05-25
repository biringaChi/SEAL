class InputValidation:
	"""
	This module performs a light input validation from
	injected payload from the Injection Zone
	"""
	def __init__(self) -> None:
		pass
	
	def validate(self, payload): 
		return payload if isinstance(payload, str) else False