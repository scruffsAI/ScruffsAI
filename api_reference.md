# API Reference

## RugDetectionAgent
### Methods
- `analyze_transaction(transaction_data)`
  - Input: Transaction JSON
  - Output: Suspicious activity flag (String)

## TransactionMonitor
### Methods
- `process(transactions)`
  - Input: List of transaction JSON objects
  - Output: Alerts for flagged transactions
