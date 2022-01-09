from NumericalMethods import NumericalMethods

f = lambda x : 5*x**(5)-2
function = NumericalMethods(f, 4)

bisection = function.bisection(-30, 34)

bisection.print()
print(f(2))
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
