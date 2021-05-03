class fullname:
    def make_name(self, firstName, lastName):
        if (type(firstName) is not str or type(lastName) is not str):
            return "first or last name input must be string."

        if (firstName.isalpha() == False or lastName.isalpha() == False):
            return 'Name input cannot have letters or special characters.'

        return firstName + ' ' + lastName

f1 = fullname()
print(f1.make_name('Luke', 'Skywalker'))
print(f1.make_name(1, 'Skywalker'))
print(f1.make_name('2', 'Alex'))