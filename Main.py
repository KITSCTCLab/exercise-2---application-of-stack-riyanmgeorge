class Evaluate:
    # Write your code here


  def __init__(self, size):
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
      # Write your code here


  def pop(self):
    # Write your code here


  def push(self, operand):
    # Write your code here


  def validate_postfix_expression(self, expression):
    # Write your code here


  def evaluate_postfix_expression(self, expression):
    # Write your code here


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix Statement')
