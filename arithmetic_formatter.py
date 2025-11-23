
def arithmetic_arranger(problems, show_answers=False):     
    arithmetic_sorter(raw_data(problems), show_answers)
    
def raw_data(problems):
    list_of_dicts = []
    new_dict = {}
    for problem in problems:
        splited_args = problem.split()
        new_dict["first arg"] = splited_args[0]
        new_dict["operator"] = splited_args[1]
        new_dict["second arg"]= splited_args[2]
        if len(new_dict["first arg"]) > 4 or len(new_dict["second arg"]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
     
            
        if len(new_dict["first arg"]) > len(new_dict["second arg"]):
            counter = len(new_dict["first arg"])
        else:
            counter = len(new_dict["second arg"])
        
            
        new_dict["lines"] = (counter+2) * "-"
        try:
            if new_dict["operator"] == "+":
                new_dict["answer"] = str(int(splited_args[0]) + int(splited_args[2]))
            elif new_dict["operator"] == "-" :
                new_dict["answer"] = str(int(splited_args[0]) - int(splited_args[2]))
            else: 
                return "Error: Operator must be '+' or '-'."
        except ValueError:
            return "Error: Numbers must only contain digits."

       
        new_dict["first arg"] = ((len(new_dict["lines"]) - len(new_dict["first arg"])) * " ") + splited_args[0]
        new_dict["second arg"] = (((len(new_dict["lines"]) - len(new_dict['second arg']) -1)) * " ") + splited_args[2]
        new_dict["answer"] = ((len(new_dict["lines"]) - len(new_dict["answer"])) * " ") + new_dict["answer"]


        list_of_dicts.append(new_dict)
        if len(list_of_dicts)> 5 :
            return 'Error: Too many problems.'
        new_dict ={}
    
    return list_of_dicts

def arithmetic_sorter(data_set, show_answers=False):
    if isinstance(data_set, list):
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
        if show_answers == True:
            for answers in data_set:
                answer = answers["answer"]
                print(answer + "    " , end="")
            print('')
        else: 
            pass
    else :
        print(data_set)


arithmetic_arranger(["3801 - 3802", "13 + 49", "11 - 111", "122 - 1222","111 - 18"])  


