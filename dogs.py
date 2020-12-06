class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        print(f'the height of dog {name}: {height}')

    def bark(self):
        print('goes woof!')

    def jump(self):
        print('jumps {} cm high! '.format(self.height * 2))


davids_dog = Dog('Rex', 50)
sarahs_dog = Dog('Teacup', 20)
davids_dog.bark()
davids_dog.jump()
