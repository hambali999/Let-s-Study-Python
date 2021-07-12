class Customer:
    def __init__(self, email, age):
        self._email = email
        self._age = age

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f'Email: {self._email} Age: {self._age}'


class Course:
    def __init__(self, code, title, fee):
        self._code = code
        self._title = title
        self._fee = fee

    @property
    def code(self):
        return self._code

    @property
    def fee(self):
        return self._fee

    def __str__(self):
        return f'Course: {self._code} Title: {self._title} Course Fee: ${self._fee:.2f}'


class Enrol:
    _age = 60
    _discount = 50 / 100

    def __init__(self, customer, course):
        self._customer = customer
        self._course = course

    def courseFee(self):
        if self._customer.age >= Enrol._age:
            return self._course.fee * Enrol._discount
        return self._course.fee

    def __str__(self):
        return f'Course: {self._course}, Customer: {self._customer}'


def test():
    customer1 = Customer('Joe', 65)
    course1 = Course('ICT162', 'OOP', 100)
    enrol1 = Enrol(customer1, course1)
    fee = enrol1.courseFee()
    print(enrol1)
    print(f'Course Fee: ${fee:,.2f}')


if __name__ == '__main__':
    test()
