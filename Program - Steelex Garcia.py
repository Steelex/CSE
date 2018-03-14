class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job, description):
        super(Employee, self).__init__(name, age)
        self.job = job
        self.description = description

    def resume(self):
        print("Employee Name: %s, Employee Age: %s, Employee Description: %s" % (self.name, self.age, self.description))


class Programmer(Person):
    def __init__(self, name, age, pay):
        super(Programmer, self).__init__(name, age)
        self.pay = pay

    def program(self):
        print("%s has successfully finished a program." % self.name)


franco = Employee("Franco", 27, "Cashier", "A short and asian male.")
franco.resume()
kindra = Programmer("Kindra", "20", 4500)
kindra.program()