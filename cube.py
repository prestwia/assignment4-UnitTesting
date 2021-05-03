class cube:
    def volume(self, a, b, c):
        if (type(a) is not int and type(a) is not float):
            return "Inputs must be type int or float."
        
        if (type(b) is not int and type(b) is not float):
            return "Inputs must be type int or float."

        if (type(c) is not int and type(c) is not float):
            return "Inputs must be type int or float."

        if (a < 0 or b < 0 or c < 0):
            return "Inputs must be positive."

        return a * b * c

c1 = cube()

print(c1.volume(1, 2, 3))
print(c1.volume(-1, 2, 3))
print(c1.volume('a', 3, 5))

        