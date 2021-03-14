from flask import Flask, abort, request, make_response, jsonify, Response, Blueprint
from database import Database

# Route Blueprint
queries_blueprint = Blueprint('queries', __name__)


# @route   POST /ping
# @desc    Healhcheck to make sure the service is responsive.
# @access  Public
# @params  None


@queries_blueprint.route("/ping", methods=["GET"])
def ping():
    return make_response("The service is up and running", 200)


# @route   GET /transaction/:transaction_id
# @desc    Gets a single transaction by Id
# @access  Public
# @params  None

@queries_blueprint.route("/transaction/<transaction_id>", methods=["GET"])
def transaction(transaction_id):
    db = Database()

    if request.method != "GET":
        abort(405, "Specified HTTP method not allowed")

    if not transaction_id:

        abort(400, "Mandatory body parameters missing or have incorrect type")

    result = db.get_transaction_by_id(transaction_id)

    if result:
        return make_response(jsonify(result), 200)

    else:
        abort(404, "Account not found")


# @route   GET /balance/:account_id
# @desc    Gets balance of an account
# @access  Public
# @params  None

@queries_blueprint.route("/balance/<account_id>", methods=["GET"])
def balance(account_id):
    db = Database()

    if request.method != "GET":
        abort(405, "Specified HTTP method not allowed")

    if not account_id:

        abort(400, "Mandatory body parameters missing or have incorrect type")

    result = db.get_balance_by_account_id(account_id)

    if result:
        return make_response(jsonify(result), 200)

    else:
        abort(404, "Account not found")


# @route   GET /max_transaction_volume
# @desc    Gets accounts with the maximum trnsactions
# @access  Public
# @params  None

@queries_blueprint.route("/max_transaction_volume", methods=["GET"])
def max_transaction_volume():

    db = Database()

    if request.method != "GET":
        abort(405, "Specified HTTP method not allowed")

    result = db.get_max_transaction_volume()

    if result:
        return make_response(jsonify(result), 200)

    else:
        abort(404, "Account not found")
