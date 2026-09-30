def validate_name(name):
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    return name

def validate_account_number(account_number):
    account_number = account_number.strip()
    if not account_number.isdigit() or len(account_number) != 10:
        raise ValueError("Account number must contain exactly 10 digits.")
    return account_number

def validate_pin(pin):
    pin = pin.strip()
    if len(pin) != 4 or not pin.isdigit():
        raise ValueError("PIN must contain exactly 4 digits.")
    return pin

def validate_amount(amount):
    try:
        value = float(amount)
    except ValueError:
        raise ValueError("Amount must be a valid number.")
    if value <= 0:
        raise ValueError("Amount must be greater than zero.")
    return value
