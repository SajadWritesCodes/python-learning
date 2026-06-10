from pydantic import BaseModel

class Transaction(BaseModel):
    symbol : str
    amount : float
    price : float
    action : str
    
