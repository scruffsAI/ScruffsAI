from ai16z_framework.utils import parse_transaction

class TransactionMonitor:
    def __init__(self, agent):
        self.agent = agent

    def process(self, transactions):
        for tx in transactions:
            result = self.agent.analyze_transaction(tx)
            if result == "Suspicious activity detected":
                print(f"Alert: {tx['id']} flagged as suspicious.")
