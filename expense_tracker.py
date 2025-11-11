
expenses = []


def main():
    print(get_inputs())

def get_inputs():
    
    commands = """
                1. ADD 
                2. SHOW ALL EXPENSES
                3. FILTER EXSPENSES BY CATEGORY
                4. TOTAL EXPENSES
                5. TOTAL EXPENSES BY CATEGORY
                6. EXIT
                """
    while True:
        command = input(commands)
        if command == '1':
            amount = int(input('How much you spend? '))
            category = input('What was it for? ')
            adding_to_list(amount, category)

        elif command == '2':
            print(expenses)

        elif command == '3':
            category = input('Which category you want to filter? ')
            print(filter_by_category(category, expenses))

        elif command == '4':
            print(total_sum(expenses))
        
        elif command =='5':
            category = input('Which category you want to filter? ')
            print(sum(map(lambda x: x['amount:'],filter_by_category(category, expenses))))
        
        elif command == '6':
            print("See ya later!")
            
            break

        else :
            print('Wrong command, please type the number of your choice.')


def adding_to_list(amount, category):
    expenses.append({'amount:': amount , 'category': category})

    return expenses

def filter_by_category(category, expenses):
    idk = lambda expense: expense['category'] == category
    
    filtered_list =list( filter(idk , expenses))

    return filtered_list
   
    
def total_sum(expenses):
    total = (sum(map(lambda expense: expense['amount:'],  expenses)))
    return total






if __name__ == '__main__':
    main()