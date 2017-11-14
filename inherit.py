class Animal(object):
    def r(self):
        print('animal is running...')
class Dog(Animal):
    def run(self):
        print('dog is running..')
class Cat(Animal):
    pass
class Tortoise(Animal):
    def run(self):
        print('tortoise is runnning')
def run_twice(animal):
    animal.run()
    animal.r()
dog=Dog()
dog.run()
run_twice(Tortoise())