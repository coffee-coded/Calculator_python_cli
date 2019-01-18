import re

print("\n\nWelcome to the calculator")
print("Type q to exit")
print("Type r to refresh everything\nType i for instructions\n")

previous = 0;
run = True
first = 0;


def perform():
    global run
    global previous
    global first
    equation = ""

    if first == 0:
        equation = input("Enter Your equation to evaluate : ")
        first = 1;
    else:
        print(previous)
        equation = input(">>>")

    if (equation == "q"):
        print("Goodbye, human.")
        run = False
    elif equation == "r":
        previous = 0
        first = 0
    elif equation == "i":
        instructions()
        previous = 0
        first = 0

    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation);
        if (previous == 0):
            previous = eval(equation)g
        else:
            previous = eval(str(previous) + equation)
        print("Result : ", previous)


def instructions():
    print("--------------------------------INSTRUCTIONS----------------------------------------")
    print("\nYour equations would look like 4+5 or 6*2, like you do in basic maths");
    print("Once you have executed your first equation, you can continue to have operation on it")
    print("just type '+7' or '*2' or your desired operation as per your requirement")
    print("Remember to type 'r' to refresh or 'q' to quit\n")
    print("------------------------------------------------------------------------------------")

while run:
    perform()
