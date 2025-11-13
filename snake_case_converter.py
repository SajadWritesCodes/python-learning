"""
Learning list comprehension by building a case converter program
"""
pascal_or_camel_cased_string = 'CongeratulationsYouSucceed!'
def convert_to_snake_cased_string(pascal_or_camel_cased_string):
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_cased_string(pascal_or_camel_cased_string))

if __name__ == '__main__':
    main()


