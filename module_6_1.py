class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        self.fed = True

        if ((self.fed == True) and (food.edible == False)):
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

        if ((self.fed == True) and (food. edible == True)):
            print(f'{self.name} съел и наелся {food.name}')
            self.fed = True

class Mammal(Animal):
    alive = False

class Predator(Animal):
    alive = True

class Plant(Animal):
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
#
print(a1.name)
print(p1.name)
#
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
