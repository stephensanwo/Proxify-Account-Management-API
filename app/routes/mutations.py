from flask import Flask, abort, request, make_response, jsonify, Response, Blueprint
from database import Database
from database.model import Transactions
from uuid import UUID


# Route Blueprint
mutations_blueprint = Blueprint('mutations', __name__)


# @route   POST /amount
# @desc    Creates a new transaction which updates the current account balance.
# @access  Public
# @params  None


@mutations_blueprint.route("/amount", methods=["POST"])
def amount():
    db = Database()
    if request.method != "POST":
        abort(405, "Specified HTTP method not allowed")

    if request.content_type != 'application/json':
        abort(415, "Specified content type not allowed")

    try:
        request_data = request.get_json()
        transaction_id = request.headers['Transaction-Id']
        account_id = request_data["account_id"]
        amount = request_data['amount']

    except:
        abort(400, "Mandatory body parameters missing or have incorrect type")

    # Validate Inputs
    if account_id == "" or transaction_id == "":
        abort(400, "Mandatory body parameters missing or have incorrect type")

    try:
        val = UUID(account_id, version=4)
    except:
        abort(400, "Mandatory body parameters missing or have incorrect type")

    try:
        val = UUID(transaction_id, version=4)
    except:
        abort(400, "Mandatory body parameters missing or have incorrect type")

    newTransaction = Transactions(
        transaction_id=transaction_id, account_id=account_id, amount=amount)

    results = db.add_new_transaction(
        newTransaction.transaction_id, newTransaction.account_id, newTransaction.amount)

    return make_response("Transaction created", 200)
