class Character:
    def __init__(self):
        self.__archetype = ''
        self.__maxMana = 100
        self.__maxHealth = 100
        self.__maxStamina = 100
        self.__mana = self.__maxMana
        self.__health = self.__maxHealth
        self.__stamina = self.__maxStamina
        self.__strength = 10
        self.__intelligence = 10
        self.__agility = 10
        self.__items = []

    # Getter methods
    def get_archetype(self):
        return self.__archetype

    def get_max_mana(self):
        return self.__maxMana

    def get_mana(self):
        return self.__mana

    def get_max_health(self):
        return self.__maxHealth

    def get_health(self):
        return self.__health

    def get_max_stamina(self):
        return self.__maxStamina

    def get_stamina(self):
        return self.__stamina

    def get_strength(self):
        return self.__strength

    def get_intelligence(self):
        return self.__intelligence

    def get_agility(self):
        return self.__agility

    def get_items(self):
        return self.__items

    # Setter methods
    def set_archetype(self, archetype):
        self.__archetype = archetype

    def set_max_mana(self, max_mana):
        self.__maxMana = max_mana
        self.__mana = max_mana

    def set_mana(self, mana):
        self.__mana = mana

    def set_max_health(self, max_health):
        self.__maxHealth = max_health
        self.__health = max_health

    def set_health(self, health):
        self.__health = health

    def set_max_stamina(self, max_stamina):
        self.__maxStamina = max_stamina
        self.__stamina = max_stamina

    def set_stamina(self, stamina):
        self.__stamina = stamina

    def set_strength(self, strength):
        self.__strength = strength

    def set_intelligence(self, intelligence):
        self.__intelligence = intelligence

    def set_agility(self, agility):
        self.__agility = agility

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    # Methods to modify stats
    def increase_max_mana(self, amount):
        self.__maxMana += amount

    def decrease_max_mana(self, amount):
        if self.__maxMana - amount >= 1:
            self.__maxMana -= amount
        else:
            self.__maxMana = 1

    def increase_mana(self, amount):
        if self.__mana + amount <= self.__maxMana:
            self.__mana += amount

    def decrease_mana(self, amount):
        if self.__mana - amount >= 0:
            self.__mana -= amount
        else:
            self.__mana = 0

    def increase_max_health(self, amount):
        self.__maxHealth += amount

    def decrease_max_health(self, amount):
        if self.__maxHealth - amount >= 1:
            self.__maxHealth -= amount
        else:
            self.__maxHealth = 1

    def increase_health(self, amount):
        if self.__health + amount <= self.__maxHealth:
            self.__health += amount

    def decrease_health(self, amount):
        if self.__health - amount >= 0:
            self.__health -= amount
        else:
            self.__health = 0

    def increase_max_stamina(self, amount):
        self.__maxStamina += amount

    def decrease_max_stamina(self, amount):
        if self.__maxStamina - amount >= 1:
            self.__maxStamina -= amount
        else:
            self.__maxStamina = 1

    def increase_stamina(self, amount):
        if self.__stamina + amount <= self.__maxStamina:
            self.__stamina += amount

    def decrease_stamina(self, amount):
        if self.__stamina - amount >= 0:
            self.__stamina
