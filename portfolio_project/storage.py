''' In this file I built my database which currently is a json file.'''
from pathlib import Path
import json, random, string


file = Path(__file__).parent /'transactions.json'

# load transactions history list
def load_transactions():
    if not file.exists() or file.stat().st_size == 0:
        transactions = []
    else:
        with open(file) as f:
            transactions = json.load(f)
    return transactions

# overwrite new transactions to file
def write_to_file(transactions):
    with open(file, 'w') as f:
        json.dump(transactions, f)

# build new transactions list + new transaction and then call write_to_file func
def add_transaction(transacton):
    transactions = load_transactions()
    transacton = transacton.model_dump()
    transacton['ID'] = id_gen()
    transactions.append(transacton)
    write_to_file(transactions)

# Generate a uniqe id for each transaction 
def id_gen():
    chars = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(chars, k=4))

# find transaction by its uniqe id 
def find_transaction(transactions, transaction_id):
    return next ((tx for tx in transactions if tx['ID']== transaction_id), None)

# remove the transaction by its id 
def remove_transaction(transaction_id):
    transactions = load_transactions()
    try:
        transactions.remove(find_transaction(transactions,transaction_id))
        write_to_file(transactions)
        return True
    except ValueError :
        return False

# show transactions file to user 
def display_transactions():
    return load_transactions()