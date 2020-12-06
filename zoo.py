from itertools import groupby
from operator import itemgetter


class Zoo:

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print('{} already found'.format(new_animal))

    def get_animals(self):
        animals = self.animals
        print(*animals, sep=", ")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            print('{} removed'.format(animal_sold))
            self.animals.remove(animal_sold)
        else:
            print('{} animal not found'.format(animal_sold))

    def sort_animals(self):

        word_list = self.animals
        print('--- YOUR ANIMALS IN {} ----'.format(self.name.upper()))
        for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
            print('-{}'.format(letter.upper()))
            for word in words:
                print(word)

    def get_groups(self, animal_in_group):
        word_list = self.animals
        print('--- THE GROUP ANIMALS OF {} ----'.format(animal_in_group.upper()))
        for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
            if letter == animal_in_group[0]:
                print('-{}'.format(letter.upper()))
                for word in words:
                    print(word)


ramat_gan_safari = Zoo('safari')

ramat_gan_safari.add_animal('geraf')
ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('cat')
ramat_gan_safari.add_animal('dog')
ramat_gan_safari.add_animal('hourse')
ramat_gan_safari.add_animal('coco')
ramat_gan_safari.add_animal('lul')
ramat_gan_safari.add_animal('geraf')

ramat_gan_safari.sell_animal('lion')

ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()

ramat_gan_safari.get_groups('coco')
