class Skill:
    """
    Represents a skill that the character can learn and use.
    """
    def __init__(self,
                  name: str,
                  attack_power_multiplier: float,
                  magic_attack_power_multiplier: float,
                  stamina_cost: int,
                  mana_cost: int):
        """
        Initializes a new skill with the specified properties.

        Args:
            name: The name of the skill.
            attack_power_multiplier: The multiplier applied to the character's attack power when using the skill.
            magic_attack_power_multiplier: The multiplier applied to the character's magic attack power when using the skill.
            stamina_cost: The amount of stamina consumed when using the skill.
            mana_cost: The amount of mana consumed when using the skill.
        """
        self.name: str = name
        self.attack_power_multiplier: float = attack_power_multiplier
        self.magic_attack_power_multiplier: float = magic_attack_power_multiplier
        self.stamina_cost: int = stamina_cost
        self.mana_cost: int = mana_cost

    # Getter methods

    def get_name(self) -> str:
        """
        Returns the name of the skill.
        """
        return self.name

    def get_attack_power(self) -> float:
        """
        Returns the attack power multiplier of the skill.
        """
        return self.attack_power_multiplier

    def get_magic_attack_power(self) -> float:
        """
        Returns the magic attack power multiplier of the skill.
        """
        return self.magic_attack_power_multiplier

    def get_stamina_cost(self) -> int:
        """
        Returns the stamina cost of the skill.
        """
        return self.stamina_cost

    def get_mana_cost(self) -> int:
        """
        Returns the mana cost of the skill.
        """
        return self.mana_cost
