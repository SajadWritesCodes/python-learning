
expenses = []


def main():
    print(get_inputs())

def get_inputs():
    
    while True:
        commend = input("'choose one of these list, you can do it by just typing the number\n' 
                         , '1. ADD   \n'
                         , '2. Filter     \n'"
                         )
        if commend == '1':
            amount = int(input('How much you spend? '))
            category = input('What was it for? ')
            adding_to_list(amount, category)
        elif commend == '2':
            category = input('Which category you want to filter? ')
            filter_by_category(category)
        else :
            break
    return expenses


def adding_to_list(amount,category):
    expenses.append({'amount:': amount , 'category': category})

    return expenses
"""
so I was trying too get commend by offering a menu 
problem : how to print a menu in input function,
then after I solve that 
I should write the filter function, it is suppose to show total expenses of filtered category

"""



















if __name__ == '__main__':
    main()