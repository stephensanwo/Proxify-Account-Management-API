
class Transactions():

    def __init__(self, transaction_id, account_id, amount):
        self.account_id = account_id
        self.transaction_id = transaction_id
        self.amount = amount

    def __str__(self):
        return f"transaction_id: {self.transaction_id} amount:{self.amount}"
