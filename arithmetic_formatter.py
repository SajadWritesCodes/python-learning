"""
def arithmetic_arranger(problems, show_answers=False):

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
"""

def arithmetic_arranger(problems):
        list_of_dicts = []
        new_dict = {}
        for problem in problems:
            splited_args = problem.split()
            new_dict["first arg"] = splited_args[0]
            new_dict["operator"] = splited_args[1]
            new_dict["second arg"]= splited_args[2]
            list_of_dicts.append(new_dict)
        return list_of_dicts
                
                



print(arithmetic_arranger(["3801 - 2", "123 + 49"]))