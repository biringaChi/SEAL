class SQLiContext:
	def __init__(self, secure_strategy) -> None:
		self.secure_strategy = secure_strategy
	
	def delegate_update_strategy(self, injected_input: str):
		return self.secure_strategy.update(injected_input)

	def delegate_error_strategy(self, injected_input: str):
		return self.secure_strategy.error(injected_input)