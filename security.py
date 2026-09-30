def authenticate(account, pin):
    return account.verify_pin(pin)

def change_pin(account, old_pin, new_pin):
    account.change_pin(old_pin, new_pin)
