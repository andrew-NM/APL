import dis

def calculate_sum(a,b):
    return a + b

dis.dis(calculate_sum)

"""
    LOAD_FAST
    Purpose: Loads a local variable onto the stack
    Operation: Takes the variable name from the function's local namespace and pushes its value onto the stack
    BINARY_ADD
    Purpose: Performs addition of the top two items on the stack
    Operation: Pops the top two values from the stack, adds them, and pushes the result back onto the stack
    RETURN_VALUE
    Purpose: Returns from the function with the top of the stack as the return value
    Operation: Pops the top value from the stack and returns it to the caller

    (PVM) Stack-Based Nature:
    1.1ast-In-First-Out (LIFO) : The PVM uses a stack where operations always work on the top elements
    2. Operand Stack: All operations pop their operands from the stack and push results back
    3. No Registers: Unlike CPU architectures, the PVM doesn't have general-purpose registers
    4. Implicit Operands: Instructions don't specify operands explicitly - they always work on stack top

"""