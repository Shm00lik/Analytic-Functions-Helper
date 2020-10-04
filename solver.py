from sympy import *
from function import Function

class Solver():
    def __init__(self, function):
        self.func = function
        func_solver = Function(self.func)
        self.derivative = func_solver.derivative()
        self.eval_derivative = func_solver.to_eval(self.derivative)

    def solve_it(self, func):
        x = Symbol('x')
        return solve(sympify(func), x)
    
    def extrem_points(self):
        return [x for x in self.solve_it(self.eval_derivative) if "i" not in str(x).lower()]
    
    def cacl_derivative(self):
        return self.derivative

