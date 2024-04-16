
from classes.spells import Spells
from classes.wizard import Wizard


harry = Wizard(
    first_name = "Harry",
    last_name = "POTTER",
    gender = "Male",
    age = 11,
    spells = [
        Spells(name="lumos", damage = 0, buff=0),
        Spells(name="wingardium leviosa", damage = 5, buff=0)
        ]
)

ron = Wizard(
    first_name = "Ron",
    last_name = "Wisley",
    gender = "Male",
    age = 11,
    spells = [
        Spells(name="lumos", damage = 0, buff=0),
        Spells(name="wingardium leviosa", damage = 5, buff=0)
        ]
)

harry.say_hello(ron)
ron.say_hello(harry)

harry.attack(ron, 1)
ron.attack(harry, 0)