import os

a = os.path.realpath(__file__)
b = os.path.dirname(a)
c = os.path.join(b, "test")

print(a)
print(b)
print(c)