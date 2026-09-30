def financial_summary(transactions):
    total_deposits = 0.0
    total_withdrawals = 0.0
    for transaction in transactions:
        if transaction["type"] == "Deposit":
            total_deposits += transaction["amount"]
        elif transaction["type"] in ("Withdrawal", "Transfer"):
            total_withdrawals += transaction["amount"]
    return {
        "total_deposits": total_deposits,
        "total_withdrawals": total_withdrawals,
        "transaction_count": len(transactions),
    }

def display_summary(summary, balance):
    print("\n========== FINANCIAL SUMMARY ==========")
    print(f"Current Balance   : ₹{balance:.2f}")
    print(f"Total Deposits    : ₹{summary['total_deposits']:.2f}")
    print(f"Total Withdrawals : ₹{summary['total_withdrawals']:.2f}")
    print(f"Transactions      : {summary['transaction_count']}")
