
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
     
            
        if len(new_dict["first arg"]) > len(new_dict["second arg"]):
            counter = len(new_dict["first arg"])
        else:
            counter = len(new_dict["second arg"])
        
            
        new_dict["lines"] = (counter+2) * "-"
        if new_dict["operator"] == "+":
            new_dict["answer"] = str(int(splited_args[0]) + int(splited_args[2]))
        else :
            new_dict["answer"] = str(int(splited_args[0]) - int(splited_args[2]))
       
        new_dict["first arg"] = ((len(new_dict["lines"]) - len(new_dict["first arg"])) * " ") + splited_args[0]
        new_dict["second arg"] = (((len(new_dict["lines"]) - len(new_dict['second arg']) -1)) * " ") + splited_args[2]
        new_dict["answer"] = ((len(new_dict["lines"]) - len(new_dict["answer"])) * " ") + new_dict["answer"]


        list_of_dicts.append(new_dict)
        new_dict ={}
    
    return list_of_dicts

def arithmetic_sorter(data_set):
    print(data_set)
    for _ in data_set:
        first_arg = _["first arg"]
        print (first_arg + "    ", end="")
    print("")
    for sec_line in data_set:
        operator = sec_line["operator"]
        second_arg = sec_line['second arg']
        print(operator+second_arg+"    ", end="")
    print()
    for lines in data_set:
        line = lines['lines']
        print(line+"    ", end="")
    print("")
    for answers in data_set:
        answer = answers["answer"]
        print(answer + "    " , end="")
    print('')


arithmetic_arranger(["3801 - 3802", "123 + 49", "11 - 111"])  


