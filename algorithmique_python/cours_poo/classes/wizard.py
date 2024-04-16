

from classes.human import Human


class Wizard(Human):

    def __init__(self, first_name, last_name, gender, age, spells):
        super().__init__(first_name, last_name, gender, age)
        self.spells = spells

    def attack(self, human, spell_index):
        spell = self.spells[spell_index]
        print(f"{self.first_name} attaque {human.first_name} avec le sort {spell.name}.")
        total_damage = (spell.damage * (self.xp/1000)) + (human.armor * (human.xp/100)) + (self.health/100)
        human.health -= total_damage
        print(f"{self.first_name} inflige {total_damage} de dégâts à {human.first_name}. (vie: {human.health})")