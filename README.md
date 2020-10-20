# Compilador
Compilador

# EBNF

    BLOCK = { COMMAND } ;
    COMMAND = ( λ | ASSIGNMENT | PRINT | IF | WHILE), "\n" ;
    ASSIGNMENT = IDENTIFIER, "=", (REL_EXPRESSION | readline, "(", ")" ) ;
    PRINT = "println", "(", REL_EXPRESSION, ")" ;
    EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;
    REL_EXPRESSION = EXPRESSION, { ("==" | ">" | "<"), EXPRESSION };
    WHILE = "while", REL_EXPRESSION, "\n", BLOCK, "end";
    IF = "if", REL_EXPRESSION, "\n", BLOCK, { ELSEIF | ELSE }, "end";
    ELSEIF = "elseif", REL_EXPRESSION, "\n", BLOCK, { ELSEIF | ELSE };
    ELSE = "else", "\n", BLOCK;
    TERM = FACTOR, { ("*" | "/" | "&&"), FACTOR } ;
    FACTOR = (("+" | "-" | "!"), FACTOR) | NUMBER | "(", REL_EXPRESSION, ")" | IDENTIFIER ;
    IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
    NUMBER = DIGIT, { DIGIT } ;
    LETTER = ( a | ... | z | A | ... | Z ) ;
    DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
    
# SYNTATIC DIAGRAM

![Alt text](Diagrama_Sintatico.png)

# HOW TO RUN

Run the code:

    $ python main.py "file.jl"

Where file.jl is a julia file that works with the ebnf (e.g):

    $ python main.py "test.jl"

Where test.jl is equal to:
    
    1+1*1/1+(--1)

The return should be the result of the operation (e.g):

    $ 3
