from aircraft import Aircraft, F16, F35
from carrier import Carrier


def main():
    tomcat = F16()
    raptor = F16()
    falcon = F16()
    desert_fox = F16()
    double_barrel = F35()
    panther = F35()
    lightning = F35()
    tornado = F35()
    typhoon = F35()

    typhoon.getType()
    typhoon.refill(20)
    typhoon.fight()
    typhoon.refill(20)
    print(typhoon.refill(20))
    print(typhoon.getStatus())
    print(typhoon.isPriority())

    nimitz = Carrier(5000,2280)

    nimitz.add(tomcat)
    nimitz.add(raptor)
    nimitz.add(falcon)
    nimitz.add(panther)
    nimitz.add(lightning)
    nimitz.add(typhoon)
    print(nimitz.getStatus())
    nimitz.fill()
    print(nimitz.getStatus())

    enterprise = Carrier(1000,500)

    enterprise.add(tomcat)
    enterprise.add(raptor)
    enterprise.add(falcon)
    enterprise.add(panther)
    enterprise.add(lightning)
    enterprise.add(typhoon)
    print(enterprise.getStatus())
    enterprise.fill()
    print(enterprise.getStatus())

    enterprise.fight(nimitz)
    print(enterprise.getStatus())
    nimitz.getStatus()


if __name__ == "__main__":
    main()