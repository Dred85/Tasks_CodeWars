<<<<<<< HEAD
class Ship:
    """Класс корабль: наполнение и экипаж"""
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft > self.crew * 1.5 + 20



Titanic = Ship(100, 20)
=======
class Ship:
    """Класс корабль: наполнение и экипаж"""
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft > self.crew * 1.5 + 20



Titanic = Ship(100, 20)
>>>>>>> Tasks_CodeWars/master
print(Titanic.is_worth_it())