
def main():

    square_root(n)


def square_root(square_target, tolerance = 1e-8, max_iteration = 100):
    root = None
    if square_target < 0:
        raise ValueError('Squar root for negative numbers is not defined')
    elif square_target == 0:
        root = 0
        print(f'The square root for {square_target} is {root}')
    elif square_target == 1 :
        root = 1
        print(f'The square root for {square_target} is {root}')
    else :
        low = 0
        high = max(1, square_target)
        for _ in range(max_iteration):
            mid = (low + high) / 2
            square_mid = mid **2
            if abs(square_target - square_mid) < tolerance:
                root = mid
                print(f'The square root of {square_target} is approximately {round(root,4)}')
                break    
            else :   
                if square_target > square_mid :
                    low = mid
                else: 
                    high = mid

        if root is None:
                print(f"Can't finde the square root in the {max_iteration} iterations")
    return root







n = 101


if __name__ == '__main__':
    main()