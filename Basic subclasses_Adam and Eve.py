class Human:
    def __init__(self, name, age):

        self.name = name
        self.age = age

class Man(Human):

    def __init__(self, name, age):

        Human.__init__(self, name, age)
        self.gender ='male'
class Woman(Human):

    def __init__(self, name, age):

        Human.__init__(self, name, age)
        self.gender = 'female'

def God():
    return [Man('Иванов', 30), Woman('Иванов', 20  )]