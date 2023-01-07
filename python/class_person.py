import random


class Person:
    shield = 10
    health = 100
    impact_strength = 20  # сила удара
    name = None

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")
        self.impact_strength = kwargs.get("impact_strength", self.impact_strength)
        self.health = kwargs.get("health", self.health)
        self.shield = kwargs.get("shield", self.shield)

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def hit(self, unit):
        now_unit_health = random.randint(0, unit.health)
        now_impact_strength = random.randint(0, self.impact_strength)
        now_unit_shield = random.randint(
            0, unit.shield if now_impact_strength < unit.shield else unit.shield
        )
        delta_unit_health = now_unit_health - now_impact_strength + now_unit_shield
        return unit.health - abs(int(delta_unit_health))

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


if __name__ == "__main__":

    win_dct = dict()

    for i in range(0, 100):
        tom = Person(name="Tom", impact_strength=50, health=100, shield=10)
        bob = Person(name="Bob", impact_strength=20, health=100, shield=50)
        step = 1
        while True:
            print(f"\nШаг {step}")
            print(f"{bob.name} бьёт {tom.name}")
            print(f"У {tom.name} {tom.health} здоровья было")
            tom.health = bob.hit(tom)
            print(f"У {tom.name} {tom.health} здоровья стало")
            if not tom.is_alive:
                print(f"{tom.name} умер")
                winner = bob
                break

            print(f"{tom.name} бьёт {bob.name}")
            print(f"У {bob.name} {bob.health} здоровья было")
            bob.health = tom.hit(bob)
            print(f"У {bob.name} {bob.health} здоровья стало")
            if not bob.is_alive:
                print(f"{bob.name} умер")
                winner = tom
                break
            step += 1

        print(f"Победил {winner.name}!")
        win_dct.setdefault(winner.name, 0)
        win_dct[winner.name] += 1

    print(win_dct)
