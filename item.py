class Item:
    def __init__(self, name, defense, attack, health, mana, stamina, strength, agility, intelligence, quantity, type):
        self.__itemName = name
        self.__defenseGiven = defense
        self.__attackGiven = attack
        self.__maxManaGiven = mana
        self.__maxHealthGiven = health
        self.__maxStaminaGiven = stamina
        self.__strengthGiven = strength
        self.__agilityGiven = agility
        self.__intelligenceGiven = intelligence
        self.__quantity = quantity  
        self.__itemType = type

    # Getter methods
    def get_item_name(self):
        return self.__itemName

    def get_defense_given(self):
        return self.__defenseGiven

    def get_attack_given(self):
        return self.__attackGiven

    def get_max_mana_given(self):
        return self.__maxManaGiven

    def get_max_health_given(self):
        return self.__maxHealthGiven

    def get_max_stamina_given(self):
        return self.__maxStaminaGiven

    def get_strength_given(self):
        return self.__strengthGiven

    def get_agility_given(self):
        return self.__agilityGiven

    def get_intelligence_given(self):
        return self.__intelligenceGiven

    def get_quantity(self):
        return self.__quantity  
      
    def get_type(self):
      return self.__itemType

    # Setter method
    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity  
