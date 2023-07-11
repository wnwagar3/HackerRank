import re

while True:
    try:
        s = input().rstrip()  # capture input, strip trailing whitespace if any
        sc, mcv, ob = s.split(";")  # split input string into separate vars to be analyzed independently
        if sc == "S":  # first case <-- splitting
            if mcv == "M":  # if a method denoted by M
                cap = ob[:-2]  # remove last 2 chars which are parens () and assign new str to cap

            if mcv == "C" or mcv == "V":  # if class or var leave ob alone and assign to cap
                cap = ob

            s = re.sub("(\w)([A-Z])", r"\1 \2", cap)  # use re.sub to make groups and assign to s, first group is
            # word chars until a capital letter encountered, then new
            # group with space inbetween group(s)
            print(s.lower())  # print 's' which is all the groups with space between in lower case

        if sc == "C":  # second case <--- concatenating
            cap = ob.title()  # assign ob to cap using .title() which capitalizes first letter in every word
            s = re.sub(r" ", r"", cap)  # use re.sub to replace spaces with empty string (remove spaces)
            q = s[:1].lower() + s[1:]  # concat first letter in lower case with rest of string still using
                                       # title case so first letter in lowercase, each new word identified
                                       # with capital letter

            if mcv == "M": # if a method print q version of string adding parens ()
                print(q + "()")

            if mcv == "C": # if a Class, print string with spaces removed, first letter is capital
                print(s)   # and every new word is indicated by capital letter, no need for 'q' step

            if mcv == "V": # if a var, print string with lower case first letter, no spaces, new words
                print(q)  # indicated by capital letter

    except EOFError: # when end of file is reached, break the loop
        break

'''
Camel Case is a naming style common in many programming languages. In Java, method and variable names typically 
start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). 
Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format

Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
The operation will either be S (split) or C (combine)
M indicates method, C indicates class, and V indicates variable
In the case of a split operation, the words will be a camel case method, class or variable name that you need to
split into a space-delimited list of words starting with a lowercase letter.
In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase 
letters that you need to combine into the appropriate camel case String. Methods should end with an empty set 
of parentheses to differentiate them from variable names.

Output Format

For each input line, your program should print either the space-delimited list of words (in the case of a split 
operation) or the appropriate camel case string (in the case of a combine operation).

Sample Input
S;M;plasticCup()
C;V;mobile phone
C;C;coffee machine
S;C;LargeSoftwareBook
C;M;white sheet of paper
S;V;pictureFrame

Sample Output
plastic cup
mobilePhone
CoffeeMachine
large software book
whiteSheetOfPaper()
picture frame
'''
