# imports are ALWAYS at the beginning of the file
from math import sqrt

line = "~" * 60
print(line)
print("\t\tQuadratic Equation Solver")
print(line)
# with 1, 4, 3 the roots should be -1 and -3
a = input("Enter the value for 'a': ")
a = int(a)
b = input("Enter the value for 'b': ")
b = int(b)
c = input("Enter the value for 'c': ")
c = int(c)

print(f"For the quadrative equation {a}x\u00b2 + {b}x + {c}")
# ( -b +/- sqrt(b^2 - 4ac) ) / 2a
x = b**2 - (4 * a * c)
ans_1 = (-b + x) / 2 * a
ans_2 = (-b - x) / 2 * a

print(ans_1, ans_2)