# Class Diagram

```text
+-----------------------+
|      BankAccount      |
+-----------------------+
| account_number        |
| name                  |
| pin                   |
| balance               |
+-----------------------+
| deposit()             |
| withdraw()            |
| verify_pin()          |
| change_pin()          |
+-----------------------+

            uses

+-----------------------+
|      Transaction      |
+-----------------------+
| transaction_type      |
| amount                |
| balance_after         |
| description           |
| date                  |
+-----------------------+
| to_dict()             |
+-----------------------+

+-----------------------+
|       Analytics       |
+-----------------------+
| financial_summary()   |
| display_summary()     |
+-----------------------+

+-----------------------+
|        Storage        |
+-----------------------+
| save_data()           |
| load_data()           |
+-----------------------+
```
