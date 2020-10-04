from solver import Solver

solver = Solver(input("Function: "))
derivative = solver.cacl_derivative()

print(derivative)
print(solver.extrem_points())
