import storage, nobitex_api



#this function build realized pnl using FIFO and save it in trade_overveiw list and build lots based on remained amounts
def lots_realized_builder():
    trade_overveiw = []
    lots = {}
    transactions = storage.load_transactions()
    total_realized_pnl = 0
    total_realized_pnl_percentage = 0
    total_spending = 0
    for tx in transactions:
        symbol = tx['symbol']
        amount = float(tx['amount'])
        price = float(tx['price'])
        if symbol not in lots and tx['action'] == 'Bought':
            lots[symbol] = [{'amount': amount,
                            'price': price
            }]
        elif symbol in lots and  tx['action'] == 'Bought':
            lots[symbol].append({'amount': amount,
                                 'price': price})
        else :
            realized = 0
            j = 0
            total_cost = 0
            trade = {'symbol':tx['symbol'],
                   'amount':tx['amount'],
                   'avg_buying_price':0,
                   'sell_price':tx['price'],
                   'total_cost': 0,
                   'total_sold' : tx['amount'] * tx['price'],
                   'realized_pnl':0 
                   }
            for i in range (len(lots[symbol])):
                if tx['amount'] > lots[symbol][j]['amount']: 
                    realized += ((float(lots[symbol][j]['amount'])*float(tx['price'])) - (float(lots[symbol][j]['amount']) * float(lots[symbol][j]['price'])))
                    tx['amount'] = tx['amount'] - lots[symbol][j]['amount']
                    total_cost += float(lots[symbol][j]['price']) * float(lots[symbol][j]['amount'])
                    lots[symbol].remove(lots[symbol][j])
                else :
                    realized +=  (float(tx['amount'])*float(tx['price'])) - (float(tx['amount']) * float(lots[symbol][j]['price']))
                    total_cost += float(lots[symbol][j]['price']) * float(tx['amount'])
                    lots[symbol][j]['amount'] = lots[symbol][j]['amount'] - float(tx['amount'])
                    if lots[symbol][j]['amount'] == 0:
                        lots[symbol].remove(lots[symbol][j])
                        break
                    else: 
                        break
            trade['avg_buying_price'] =round(total_cost/trade['amount'],2)
            trade['realized_pnl'] += realized
            total_realized_pnl += realized
            trade['total_cost'] = total_cost
            total_spending += total_cost
            trade['realized_pnl%'] =(round((realized/total_cost)*100, 2))
            trade_overveiw.append(trade)  
    total_realized_pnl_percentage = round((total_realized_pnl / total_spending ) *100,2)
    trade_overveiw.append({'total spent' :total_spending,
                               'total realized pnl': total_realized_pnl,
                               'total realized pnl%': total_realized_pnl_percentage})
    
    return lots , trade_overveiw

def portfolio_builder():
    portfolio = {}
    total_unrealized_pnl= 0
    portfolio_total_value = 0
    total_unrealized_pnl_percentage = 0
    total_spent = 0
    lots = lots_realized_builder()[0]
    currency = nobitex_api.get_fiatcurrency_price('USDT')
    for symbol in lots:
        current_price = nobitex_api.current_price(symbol,currency)
        total_amount = 0
        total_cost = 0
        avg_price = 0
        
        for tx in lots[symbol] :
            amount = float(tx['amount'])
            total_amount += amount
            price = float(tx['price'])
            total_cost += price * amount
            avg_price = round(total_cost/total_amount,2)
            portfolio[symbol] = {'amount':total_amount,
                              'avg_price':avg_price,
                              'total_cost' : total_cost
                              }
        portfolio[symbol]['current_price'] = current_price
        portfolio_total_value += round(portfolio[symbol]['amount'] * current_price,2)
        total_spent += total_cost
        portfolio[symbol]['unrealized_profit'] = round(portfolio[symbol]['amount'] * (current_price - portfolio[symbol]['avg_price']),2)
        portfolio[symbol]['unrealized_profit%'] = round((portfolio[symbol]['unrealized_profit']/total_cost) * 100,2)
        total_unrealized_pnl+= portfolio[symbol]['unrealized_profit']

    total_unrealized_pnl_percentage = round((total_unrealized_pnl/portfolio_total_value)*100,2)
    porfolio_overveiw = {'total value':portfolio_total_value,
                         'total spent':total_spent,
                         'total unrealized pnl':total_unrealized_pnl,
                         'total unrealized pnl %':total_unrealized_pnl_percentage
                         }

    return portfolio, porfolio_overveiw

def show_portfolio():
    return portfolio_builder()    


def show_realized_pnl():
    return lots_realized_builder()[1]



