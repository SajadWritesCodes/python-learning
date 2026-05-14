
def collatz(user_choice):
    if user_choice % 2 == 0:
       return user_choice // 2
    else:
        return (user_choice * 3) +1


def ask_user():
    user_choice = 0

    while user_choice < 1:
        try:
            user_choice = int(input("Write a positive integer number: "))
            if user_choice < 1:
                print("You should type a positive integer number: ")
        except ValueError:
            print("You should type a positive integer number: ")

    return user_choice

def collatz_seq_builder(user_choice):
    collatz_seq = [user_choice]
    while user_choice != 1:
        user_choice = collatz(user_choice)
        collatz_seq.append(user_choice)
  
    return collatz_seq


def main():
    print(collatz_seq_builder(ask_user()))


if __name__ == "__main__":
    main()