from item import *
from skill import *

class Character:
    """
    Represents the player character in the game.
    """

    def __init__(self):
        """
        Initializes a new character with default stats and empty inventories.
        """

        self.__archetype: str = ""
        self.__max_mana: int = 100
        self.__max_health: int = 100
        self.__max_stamina: int = 100
        self.__mana: int = self.__max_mana
        self.__health: int = self.__max_health
        self.__stamina: int = self.__max_stamina
        self.__strength: int = 10
        self.__intelligence: int = 10
        self.__agility: int = 10
        self.__items: list[Item] = []
        self.__skills: list[Skill] = []
        

    # Getter methods
    def get_archetype(self) -> str:
        """
        Returns the character's archetype (e.g., Fighter, Mage, Rogue).
        """
        return self.__archetype

    def get_max_mana(self) -> int:
        """
        Returns the character's maximum mana pool.
        """
        return self.__maxMana

    def get_mana(self) -> int:
        """
        Returns the character's current mana.
        """
        return self.__mana

    def get_max_health(self) -> int:
        """
        Returns the character's maximum health pool.
        """
        return self.__maxHealth

    def get_health(self) -> int:
        """
        Returns the character's current health.
        """
        return self.__health

    def get_max_stamina(self) -> int:
        """
        Returns the character's maximum stamina pool.
        """
        return self.__maxStamina

    def get_stamina(self) -> int:
        """
        Returns the character's current stamina.
        """
        return self.__stamina

    def get_strength(self) -> int:
        """
        Returns the character's strength stat.
        """
        return self.__strength

    def get_intelligence(self) -> int:
        """
        Returns the character's intelligence stat.
        """
        return self.__intelligence

    def get_agility(self) -> int:
        """
        Returns the character's agility stat.
        """
        return self.__agility

    def get_items(self) -> [Item]:
        """
        Returns a list of all items in the character's inventory.
        """
        return self.__items

    def get_skills(self) -> [Skill]:
        """
        Returns a list of all skills possessed by the character.
        """
        return self.__skills
    
    # Setter methods
    def set_archetype(self, archetype: str) -> None:
        """
        Sets the character's archetype (e.g., Fighter, Mage, Rogue).
        """
        self.__archetype = archetype

    def set_max_mana(self, max_mana: int) -> None:
        """
        Sets the character's maximum mana pool and updates current mana to the new maximum.
        """
        self.__maxMana = max_mana
        self.__mana = max_mana

    def set_mana(self, mana: int) -> None:
        """
        Sets the character's current mana.
        """
        self.__mana = mana

    def set_max_health(self, max_health: int) -> None:
        """
        Sets the character's maximum health pool and updates current health to the new maximum.
        """
        self.__maxHealth = max_health
        self.__health = max_health

    def set_health(self, health: int) -> None:
        """
        Sets the character's current health.
        """
        self.__health = health
        
    def set_max_stamina(self, max_stamina: int) -> None:
        """
        Sets the character's maximum stamina pool and updates current stamina to the new maximum.
        """
        self.__maxStamina = max_stamina
        self.__stamina = max_stamina

    def set_stamina(self, stamina: int) -> None:
        """
        Sets the character's current stamina.
        """
        self.__stamina = stamina

    def set_strength(self, strength: int) -> None:
        """
        Sets the character's strength stat.
        """
        self.__strength = strength

    def set_intelligence(self, intelligence: int) -> None:
        """
        Sets the character's intelligence stat.
        """
        self.__intelligence = intelligence

    def set_agility(self, agility: int) -> None:
        """
        Sets the character's agility stat.
        """
        self.__agility = agility

    def add_item(self, item: Item) -> None:
        """
        Adds the given item to the character's inventory.
        """
        self.__items.append(item)

    def remove_item(self, item: Item) -> None:
        """
        Removes the given item from the character's inventory.
        """
        self.__items.remove(item)
        
    def add_skill(self, skill: Skill) -> None:
        """
        Adds the given skill to the character's list of known skills.
        """
        self.__skills.append(skill)

    def remove_skill(self, skill: Skill) -> None:
        """
        Removes the given skill from the character's list of known skills.
        """
        self.__skills.remove(skill)


    # Methods to modify stats
    
    def increase_max_mana(self, amount: int) -> None:
        """
        Increases the character's maximum mana pool by the specified amount.
        """
        self.__maxMana += amount

    def decrease_max_mana(self, amount: int) -> None:
        """
        Decreases the character's maximum mana pool by the specified amount, ensuring it remains at least 1.
        """
        if self.__maxMana - amount >= 1:
            self.__maxMana -= amount
        else:
            self.__maxMana = 1

    def increase_mana(self, amount: int) -> None:
        """
        Increases the character's current mana by the specified amount, ensuring it does not exceed the maximum.
        """
        if self.__mana + amount <= self.__maxMana:
            self.__mana += amount

    def decrease_mana(self, amount: int) -> None:
        """
        Decreases the character's current mana by the specified amount, ensuring it remains non-negative.
        """
        if self.__mana - amount >= 0:
            self.__mana -= amount
        else:
            self.__mana = 0

    def increase_max_health(self, amount: int) -> None:
        """
        Increases the character's maximum health pool by the specified amount.
        """
        self.__maxHealth += amount

    def decrease_max_health(self, amount: int) -> None:
        """
        Decreases the character's maximum health pool by the specified amount, ensuring it remains at least 1.
        """
        if self.__maxHealth - amount >= 1:
            self.__maxHealth -= amount
        else:
            self.__maxHealth = 1

    def increase_health(self, amount: int) -> None:
        """
        Increases the character's current health by the specified amount, ensuring it does not exceed the maximum.
        """
        if self.__health + amount <= self.__maxHealth:
            self.__health += amount

    def decrease_health(self, amount: int) -> None:
        """
        Decreases the character's current health by the specified amount, ensuring it remains non-negative.
        """
        if self.__health - amount >= 0:
            self.__health -= amount
        else:
            self.__health = 0

    def increase_max_stamina(self, amount: int) -> None:
        """
        Increases the character's maximum stamina pool by the specified amount.
        """
        self.__maxStamina += amount

    def decrease_max_stamina(self, amount: int) -> None:
        """
        Decreases the character's maximum stamina pool by the specified amount, ensuring it remains at least 1.
        """
        if self.__maxStamina - amount >= 1:
            self.__maxStamina -= amount

    def increase_stamina(self, amount: int) -> None:
        """
        Increases the character's current stamina by the specified amount, ensuring it does not exceed the maximum.
        """
        if self.__stamina + amount <= self.__maxStamina:
            self.__stamina += amount

    def decrease_stamina(self, amount: int) -> None:
        """
        Decreases the character's current stamina by the specified amount, ensuring it remains non-negative.
        """
        if self.__stamina - amount >= 0:
            self.__stamina -= amount
        else:
            self.__stamina = 0

    def increase_strength(self, amount: int) -> None:
        """
        Increases the character's strength stat by the specified amount.
        """
        self.__strength += amount

    def decrease_strength(self, amount: int) -> None:
        """
        Decreases the character's strength stat by the specified amount, ensuring it remains at least 1.
        """
        if self.__strength - amount >= 1:
            self.__strength -= amount
        else:
            self.__strength = 1

    def increase_intelligence(self, amount: int) -> None:
        """
        Increases the character's intelligence stat by the specified amount.
        """
        self.__intelligence += amount

    def decrease_intelligence(self, amount: int) -> None:
        """
        Decreases the character's intelligence stat by the specified amount, ensuring it remains at least 1.
        """
        if self.__intelligence - amount >= 1:
            self.__intelligence -= amount
        else:
            self.__intelligence = 1

    def increase_agility(self, amount: int) -> None:
        """
        Increases the character's agility stat by the specified amount.
        """
        self.__agility += amount

    def decrease_agility(self, amount: int) -> None:
        """
        Decreases the character's agility stat by the specified amount, ensuring it remains at least 1.
        """
        if self.__agility - amount >= 1:
            self.__agility -= amount
        else:
            self.__agility = 1