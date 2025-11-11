
expenses = []


def main():
    print(get_inputs())

def get_inputs():
    
    commands = """
                1. ADD 
                2. FILTER BY CATEGORY
                3. TOTAL SPENDING
                4. TOTAL SPENDING BY CATEGORY
                """
    while True:
        command = input(commands)
        if command == '1':
            amount = int(input('How much you spend? '))
            category = input('What was it for? ')
            adding_to_list(amount, category)
        elif command == '2':
            category = input('Which category you want to filter? ')
            filter_by_category(category)
        else :
            break
    return expenses


def adding_to_list(amount,category):
    expenses.append({'amount:': amount , 'category': category})

    return expenses
"""
 
I should write the filter function, it is suppose to show total expenses of filtered category

"""



















if __name__ == '__main__':
    main()