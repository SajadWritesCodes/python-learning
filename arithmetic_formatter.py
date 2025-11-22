"""
def arithmetic_arranger(problems, show_answers=False):

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
"""

def arithmetic_arranger(problems):
    arithmetic_sorter(raw_data(problems))
    pass
def raw_data(problems):
    list_of_dicts = []
    new_dict = {}
    for problem in problems:
        splited_args = problem.split()
        new_dict["first arg"] = splited_args[0]
        new_dict["operator"] = splited_args[1]
        new_dict["second arg"]= splited_args[2]
        if new_dict["operator"] == "+":
            new_dict["answer"] = str(int(splited_args[0]) + int(splited_args[2]))
        else :
            new_dict["answer"] = str(int(splited_args[0]) - int(splited_args[2]))
            
        if len(new_dict["first arg"]) > len(new_dict["second arg"]):
            counter = len(new_dict["first arg"])
        else:
            counter = len(new_dict["second arg"])
            
        new_dict["lines"] = (counter+2) * "-"
        list_of_dicts.append(new_dict)
        new_dict ={}
    
    return list_of_dicts

def arithmetic_sorter():
    
                
                



print(raw_data(["3801 - 2", "123 + 49"]))