card_number = '6037 6916 4691 4168'

def main():
    card_validator(card_number)


def card_validator(card_number):
    card_translation = str.maketrans({' ':'', '-':''})
    translated_c_n = card_number.translate(card_translation)
    reversed_translated_cn = translated_c_n[-1::-1]
    
    def even_sum():
        even_a = 0
        evens = reversed_translated_cn [::2]
        for digits in evens:
            even_a += int(digits)
        return even_a
    def odds_sum():
        odds_a = 0
        odds = reversed_translated_cn [1::2]
        for digits in odds:
            odds_a += int(digits)
            if odds_a // 10  == 0:
                pass
            else: 
                odds_a += odds_a // 10 + odds_a % 10
        return odds_a
    if (even_sum() + odds_sum())%10 == 0:
        print('VALID!')
    else:
        print('INVALID!')
    

if __name__ == '__main__':
    main()