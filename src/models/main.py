from NumericalMethods import NumericalMethods

function = NumericalMethods(lambda x : 2*x-2, 3)

bisection = function.bisection(-30, 34)

bisection.print()
# b_1 = bisection.evaluate_once()
# print(b_1)
# b_2 = b_1.evaluate_once()
# b_3 = b_2.evaluate_once()
# 
# print(bisection)
# print(b_1)
# print(b_2)
# print(b_3)
# bisection.evaluate_once()
