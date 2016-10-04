class Printer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print 'Name:', self.name
        print 'Age:', self.age


class Demo:
    greetings = "Hello world!"

    @classmethod
    def display(cls):
        print cls.greetings
        obj = Printer('Robert', 36)
        obj.display()


if __name__ == '__main__':
    Demo.display()