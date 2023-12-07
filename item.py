class Item:
    """
    Represents an item in the game that can be equipped or used by the character.
    """

    def __init__(self,
                  name: str,
                  defense: int,
                  attack: int,
                  health: int,
                  mana: int,
                  stamina: int,
                  strength: int,
                  agility: int,
                  intelligence: int,
                  quantity: int,
                  type: str):
        """
        Initializes a new item with the specified properties.

        Args:
            name: The name of the item.
            defense: The defense bonus granted by the item.
            attack: The attack bonus granted by the item.
            health: The maximum health bonus granted by the item.
            mana: The maximum mana bonus granted by the item.
            stamina: The maximum stamina bonus granted by the item.
            strength: The strength bonus granted by the item.
            agility: The agility bonus granted by the item.
            intelligence: The intelligence bonus granted by the item.
            quantity: The quantity of the item.
            type: The type of the item (e.g., weapon, armor, consumable).
        """

        self.__itemName: str = name
        self.__defenseGiven: int = defense
        self.__attackGiven: int = attack
        self.__maxHealthGiven: int = health
        self.__maxManaGiven: int = mana
        self.__maxStaminaGiven: int = stamina
        self.__strengthGiven: int = strength
        self.__agilityGiven: int = agility
        self.__intelligenceGiven: int = intelligence
        self.__quantity: int = quantity
        self.__itemType: str = type


    # Getter methods
    def get_item_name(self) -> str:
        """
        Returns the name of the item.
        """
        return self.__itemName

    def get_defense_given(self) -> int:
        """
        Returns the defense bonus granted by the item.
        """
        return self.__defenseGiven

    def get_attack_given(self) -> int:
        """
        Returns the attack bonus granted by the item.
        """
        return self.__attackGiven

    def get_max_mana_given(self) -> int:
        """
        Returns the maximum mana bonus granted by the item.
        """
        return self.__maxManaGiven

    def get_max_health_given(self) -> int:
        """
        Returns the maximum health bonus granted by the item.
        """
        return self.__maxHealthGiven

    def get_max_stamina_given(self) -> int:
        """
        Returns the maximum stamina bonus granted by the item.
        """
        return self.__maxStaminaGiven

    def get_strength_given(self) -> int:
        """
        Returns the strength bonus granted by the item.
        """
        return self.__strengthGiven

    def get_agility_given(self) -> int:
        """
        Returns the agility bonus granted by the item.
        """
        return self.__agilityGiven

    def get_intelligence_given(self) -> int:
        """
        Returns the intelligence bonus granted by the item.
        """
        return self.__intelligenceGiven

    def get_quantity(self) -> int:
        """
        Returns the quantity of the item.
        """
        return self.__quantity

    def get_type(self) -> str:
        """
        Returns the type of the item (e.g., weapon, armor, consumable).
        """
        return self.__itemType

    def set_quantity(self, new_quantity: int) -> None:
        """
        Sets the quantity of the item to the specified value.
        """
        self.__quantity = new_quantity
