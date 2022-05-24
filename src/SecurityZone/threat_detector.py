class ThreatDetector:
	"""
	A strategy pattern to detect payload type
	"""
	def detect(self) -> None:
		pass

class UpdateThreat(ThreatDetector):
	def detect(self) -> None:
		print("Scanning for UPDATE-based payload.... \n Scan complete!")

class ErrorThreat(ThreatDetector):
	def detect(self) -> None:
		print("Scanning for ERROR-based payload... \n Scan complete")

class ThreatHandler():
	def __init__(self, payload) -> None:
		self.payload = payload
		
	def handle(self, ThreatDetector) -> None:
		return ThreatDetector.detect(self)