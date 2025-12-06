import ast

code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))

"""
 targets=[
                Name(id='y', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=Constant(value=4),
                    op=Mult(),
                    right=Constant(value=5)),
                op=Sub(),
                right=Constant(value=3)))])

"""

"""
multiplication node
BinOp with left Constant 4 op Mult right Constant 5

subtraction node
BinOp with left the above BinOp op Sub right Constant 3
"""