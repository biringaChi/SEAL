class ThreatDetector:
	"""
	This module defines the detection of In-band SQL threat patterns using a simple polymorphic technique.
	"""
	def detect(self) -> None:
		pass

class UpdateThreat(ThreatDetector):
	def detect(self) -> None:
		print("Scanning for UPDATE-based payload.... \n Scan complete!")

class ErrorThreat(ThreatDetector):
	def detect(self) -> None:
		print("Scanning for ERROR-based payload... \n Scan complete!")

class ThreatHandler():
	def __init__(self, payload) -> None:
		self.payload = payload
		
	def handle(self, ThreatDetector) :
		return ThreatDetector.detect(self)