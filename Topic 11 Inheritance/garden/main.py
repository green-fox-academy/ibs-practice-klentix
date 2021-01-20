from the_garden import *

def main():
    garden = Garden()
    flower1 = Flower("yellow")
    flower2 = Flower("blue")
    tree1 = Tree("purple")
    tree2 = Tree("orange")

    garden.add(flower1)
    garden.add(flower2)
    garden.add(tree1)
    garden.add(tree2)

    garden.info()
    garden.water(40)
    garden.water(70)


if __name__ == '__main__':
    main()