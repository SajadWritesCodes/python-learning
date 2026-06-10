from data_model import Transaction
from fastapi import FastAPI
import storage, portfolio

app = FastAPI()

@app.post('/Add_Transaction')
async def add_trans(log: Transaction):
    storage.add_transaction(log)

    return {
    "message": "Transaction added successfully",
    "Transaction": log
}

@app.post('/Delete_Transaction')
async def delete_trans(transaction_id: str):
        if storage.remove_transaction(transaction_id):
            return  {'message': 'Transaction removed succussfully'} 
        else:
            return {'message':'Id not found'}
        
@app.get('/Transaction_History')
async def show_transactions_history():
     result = storage.display_transactions()
     return {'Your history is': result}
    
@app.get('/Portfolio')
async def display_portfolio():
     result = portfolio.show_portfolio()
     return {'message':result}
@app.get('/Realized pnl')
async def display_realized_pnl():
     result = portfolio.show_realized_pnl()
     return {'message':result}