class Skill:
    def __init__(self, name, attackPowerMul, magicAttackPowerMul, staminaCost, manaCost):
        self.name = name
        self.attackP = attackPowerMul
        self.magAttackP = magicAttackPowerMul
        self.staminaCost = staminaCost
        self.manaCost = manaCost

    # Getter methods
    def get_name(self):
        return self.name

    def get_attack_power(self):
        return self.attackP

    def get_magic_attack_power(self):
        return self.magAttackP

    def get_stamina_cost(self):
        return self.staminaCost

    def get_mana_cost(self):
        return self.manaCost
