# Part of the code was made with ideas from another student

def main():

    print("starting calculator")

    prev_list = []
    result = calc_operations(prev_list)

    while True:
        if result != None:
            prev_list.append(result)
        result = calc_operations(prev_list)
        

def calc_operations(prev_ans):
    op_selection = input("\nSelect operation: Addition(+), Subtraction(-), Multiplication(*), Division(/), Previous Answers, or Quit\npycalc>>>")
    if op_selection == "Addition" or op_selection == "addition" or op_selection == "+" or op_selection == "Subtraction" or op_selection == "subtraction" or op_selection == "-" or op_selection == "Multiplication" or op_selection == "multiplication" or op_selection == "*" or op_selection == "Division" or op_selection == "division" or op_selection == "/":
        if op_selection == "Addition" or op_selection == "addition" or op_selection == "+":
            usr_args = input("Enter 2 numbers seperated by a space\naddition>>>")
            args_split = usr_args.split(" ")
            while len(args_split) != 2 or not args_split[0].isnumeric() or not args_split[1].isnumeric():
                print("Please enter 2 numbers seperated by a space (ex: 24 53)\n")
                usr_args = input("Enter 2 numbers seperated by a space\naddition>>>")
                args_split = usr_args.split(" ")
            result = (float(args_split[0]) + float(args_split[1]))
        elif op_selection == "Subtraction" or op_selection == "subtraction" or op_selection == "-":
            usr_args = input("Enter 2 numbers seperated by a space\nsubtraction>>>")
            args_split = usr_args.split(" ")
            while len(args_split) !=2 or not args_split[0].isnumeric() or not args_split[1].isnumeric():
                print("Please enter 2 numbers seperated by a space (ex: 24 53)\n")
                usr_args = input("Enter 2 numbers seperated by a space\nsubtraction>>>")
                args_split = usr_args.split(" ")
                print("Please enter 2 numbers seperated by a space (ex: 24 53)\n")
            result = (float(args_split[0]) - float(args_split[1]))
        elif op_selection == "Multiplication" or op_selection == "multiplication" or op_selection == "*":
            usr_args = input("Enter 2 numbers seperated by a space\nmultiplication>>>")
            args_split = usr_args.split(" ")
            while len(args_split) != 2 or not args_split[0].isnumeric() or not args_split[1].isnumeric():
                print("Please enter 2 numbers seperated by a space (ex: 24 53)\n")
                usr_args = input("Enter 2 numbers seperated by a space\nmultiplication>>>")
                args_split = usr_args.split(" ")
            result = (float(args_split[0]) * float(args_split[1]))
        elif op_selection == "Division" or op_selection == "division" or op_selection == "/":
            usr_args = input("Enter 2 numbers seperated by a space\ndivision>>>")
            args_split = usr_args.split(" ")
            while len(args_split) != 2 or not args_split[0].isnumeric() or not args_split[1].isnumeric():
                print("Please enter 2 numbers seperated by a space (ex: 24 53)\n")
                usr_args = input("Enter 2 numbers seperated by a space\ndivision>>>")
                args_split = usr_args.split(" ")
            result = (float(args_split[0]) / float(args_split[1]))
        print(result)
        return result
    elif op_selection == "quit" or op_selection == "q":
        quit()
    elif op_selection == "Previous Answers" or op_selection == "previous answers":
        index = input("please input a number for which answer to display, 1 being the most recent answer and answers getting older as the number increases\nanswer index>>>")
        print(prev_ans[-abs(int(index))])
    else:
        print("Please enter one of the operations provided")

if __name__ == "__main__":
    main()