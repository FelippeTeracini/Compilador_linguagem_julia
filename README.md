# Compilador
Compilador

# EBNF

    EXPRESSION = TERM, {("+"|"-"), TERM};
    TERM = FACTOR, {("*"|"/"), FACTOR};
    FACTOR = ("+" | "-") FACTOR | "(" EXPRESSION ")" | NUMBER ;
    NUMBER = DIGIT, {DIGIT};
    Digit = 0|1|2|3|4|5|6|7|8|9;


# SYNTATIC DIAGRAM

![Alt text](Diagrama_Sintatico.png)

# HOW TO RUN

Run the code:

    $ python main.py "file.jl"

Where file.jl is a julia file containing mathematical operations containing +, -, *, /, ( and ) operators (e.g):

    $ python main.py "test.jl"

Where test.jl is equal to:
    
    1+1*1/1+(--1)

The return should be the result of the operation (e.g):

    $ 3
