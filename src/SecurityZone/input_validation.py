class InputValidation:
	def __init__(self) -> None:
		pass
	
	def validate(self, payload) -> str: 
		return payload if isinstance(payload, str) else False