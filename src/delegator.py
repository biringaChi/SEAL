import sys
sys.path.append(".")

from SecurityZone.context import SQLiContext
from src.SecurityZone.input_validation import InputValidation
from src.SecurityZone.threat_detector import ThreatHandler, UpdateThreat, ErrorThreat
from SecurityZone.factory import FactoryHandler, UpdateFactory, ErrorFactory

class Delegator:
	"""
	This module defines the delegation of security strategies.
	"""
	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()

	def delegate(input: str):
		payload = InputValidation().validate(input)
		if len(payload) >= 7:
			update_threat = ThreatHandler(payload).handle(UpdateThreat)
			factory = FactoryHandler().handle(UpdateFactory)
			out =  SQLiContext(factory).delegate_update_strategy(payload)
			return out
		else: 
			error_threat = ThreatHandler(payload).handle(ErrorThreat)
			factory = FactoryHandler().handle(ErrorFactory)
			out =  SQLiContext(factory).delegate_error_strategy(payload)
			return out