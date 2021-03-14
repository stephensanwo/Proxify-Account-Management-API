import sqlite3
import json


class Database(object):

    def __init__(self):
        """initialize  connection """
        """
        creates a db
        """
        try:
            # use our connection values to establish a connection

            self.connection = sqlite3.connect('database.db')
            self.cursor = self.connection.cursor()
            self.create_tables()

        except Exception as e:
            print(e)

    def create_tables(self):
        # create tables
        self.cursor.execute(
            'CREATE TABLE transactions (account_id TEXT, transaction_id TEXT, amount INT, balance INT)')
        self.connection.commit()

    def add_new_transaction(self, transaction_id, account_id, amount):

        # Get current balance
        query = f"SELECT * FROM transactions WHERE account_id = '{account_id}';"

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        if results:
            balance_list = []
            for result in results:
                balance_list.append(result[2])
                balance = sum(balance_list) + amount
        else:
            balance = amount

        # Get transaction
        query = f"SELECT * FROM transactions WHERE transaction_id = '{transaction_id}';"

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        if result:
            transactions = f"""UPDATE transactions SET amount = '{amount}', balance = '{balance}' """

            self.cursor.execute(transactions)
            self.connection.commit()

        else:

            transactions = f"""INSERT INTO transactions(transaction_id, account_id, amount, balance) VALUES ('{transaction_id}', '{account_id}','{amount}', '{balance}');"""

            self.cursor.execute(transactions)
            self.connection.commit()

        result = {"balance": balance}
        return result

    def get_transaction_by_id(self, transaction_id):

        transaction = f"SELECT * FROM transactions WHERE transaction_id = '{transaction_id}'"

        self.cursor.execute(transaction)
        results = self.cursor.fetchone()
        self.connection.commit()

        if results:

            result = {"account_id": results[0], "amount": int(results[2])}

            return result

        else:
            return None

    def get_balance_by_account_id(self, account_id):

        # Get balance
        query = f"SELECT * FROM transactions WHERE account_id = '{account_id}';"

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        if results:
            balance_list = []
            for result in results:
                balance_list.append(result[2])

            balance = int(sum(balance_list))

            self.connection.commit()

            result = {"balance": balance}

            return result

        else:
            return None

    def get_max_transaction_volume(self):

        count = "SELECT COUNT(account_id), account_id FROM transactions GROUP BY account_id  ORDER BY COUNT('COUNT(account_id)') DESC"
        self.cursor.execute(count)
        count = self.cursor.fetchall()

        result = {
            "maxVolume": count[0][0],
            "accounts": []
        }

        for item in count:

            if item[0] == result["maxVolume"]:
                result['accounts'].append(item[1])

        return result
