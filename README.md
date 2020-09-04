# Compilador
Compilador

# EBNF

    Expression = Term, {("+"|"-"), Term};
    Term = Number, {("*"|"/"), Number};
    Number = Digit, {Digit};
    Digit = 0|1|2|3|4|5|6|7|8|9;

# SYNTATIC DIAGRAM

![Alt text](Diagrama_Sintatico.png)

# HOW TO RUN

Run the code:

    $ python main.py "operation"

Where operation is a mathematical operation containing +, -, * and / operators (e.g):

    $ python main.py "1 + 1"

The return should be the result of the operation (e.g):

    $ 2

Alternatively it is also possible to use a text file to represent the input. To do that,
write the operation on the text file and then run the following code:

    $ python main.py < example.txt
