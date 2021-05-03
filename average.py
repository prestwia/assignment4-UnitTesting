class average:
    def average_list(self, l1):
        if (len(l1) == 0):
            return "List must be populated."

        sum = 0
        for num in l1:
            if (type(num) is not int and type(num) is not float):
                return "List elements must by int or float."

            sum += num
        return sum / len(l1)

avg = average()

print(avg.average_list([1, 2, 3, 4, 5]))
print(avg.average_list(['a', 2, 4]))
print(avg.average_list([]))