import sys
sys.path.append(".")

from src.SecurityZone.secure_context import SQLiContext
from src.SecurityZone.input_validation import InputValidation
from src.SecurityZone.threat_detector import ThreatHandler, UpdateThreat, ErrorThreat
from src.SecurityZone.secure_factory import FactoryHandler, UpdateFactory, ErrorFactory

class Delegator:
	"""
	This module defines the delegation of security strategies.
	"""
	def delegate(input):
		payload = InputValidation().validate(input)
		if len(payload) >= 5:
			update_threat = ThreatHandler(payload).handle(UpdateThreat)
			factory = FactoryHandler().handle(UpdateFactory)
			out =  SQLiContext(factory).delegate_update_strategy(payload)
			return out
		else: 
			error_threat = ThreatHandler(payload).handle(ErrorThreat)
			factory = FactoryHandler().handle(ErrorFactory)
			out =  SQLiContext(factory).delegate_error_strategy(payload)
			return out