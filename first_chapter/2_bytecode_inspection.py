import dis

#define a python function square(x) that return the square of its input x (i.e.., x * x).
def square(x):
    return x*x

#use the dis module (import dis; dis.dis(square)) to inspect its bytecode
#dentify which bytecode instructions correspond to the multiplication operation => BINARY_OP 5
dis.dis(square)

#how does this copare to BINARY_ADD instruction seen in the add function example ? => BINARY_OP 0 

#==================================================
#Now define a function multiply(a,b) thar returns the product of a and b disassemble its bytecode and compare it with the add() function example from the chapter. note any similarities or differences in the bytecode instructions for arithimitic operations.
def multiply(a, b):
    return a * b
dis.dis(multiply)

#add() and multiply() use the same structure.
#The only difference is the operation code inside BINARY_OP.