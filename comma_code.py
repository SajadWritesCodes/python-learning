test = ['apples', 'banananas', 'tufo', 'cats', 'dog', 'cow']

def string_builder(target_list):
    first_part = ''
    second_part = ''
    compelete_str = ''
    if len(target_list) > 1:
        for i in range(len(target_list)-2):
            first_part += target_list[i] + ',' + ' ' 

        second_part = target_list[-2] + ' ' + 'and' + ' ' + target_list[-1]
        complete_str = first_part + second_part
    elif len(target_list) == 1:
        complete_str = target_list[0]

    else: 
        complete_str = None


    return  complete_str

def main():

    print(f"'{string_builder(test)}'")

if __name__=='__main__':
    main()