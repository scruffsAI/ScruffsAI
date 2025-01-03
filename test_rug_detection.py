import unittest
from agents.rugdetection_agent import RugDetectionAgent

class TestRugDetection(unittest.TestCase):
    def setUp(self):
        self.agent = RugDetectionAgent()

    def test_analyze_transaction(self):
        tx = {"from": "0xabc", "to": "0xdef", "value": 1000}
        result = self.agent.analyze_transaction(tx)
        self.assertIn("Suspicious", result)
