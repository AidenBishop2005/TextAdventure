from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui import *
from pynput.keyboard import *
from character import *
from item import *
from skill import *
import csv
import pickle

class gameLogic(QMainWindow):
    """
    This class represents the main game logic for the player's adventure.
    """

    def __init__(self):
        """
        Initializes the game logic class.
        Sets up the UI and initial state of the game.
        """
        super().__init__()

        self.__player: Character = Character()  # Player character object
        self.__curQuestion: str = ""  # Current question being asked to the player
        self.__traveling: bool = False  # Flag indicating if player is traveling between areas
        self.__curAreaId: int = 1  # Current area ID
        self.__curChoices: list[str] = []  # List of current choices available to the player
        self.__tempEquInv: list[str] = []  # Temporary equipment inventory list (used for switching items)
        self.__tempConInv: list[str] = []  # Temporary consumable inventory list (used for switching items)
        self.__tempMiscInv: list[str] = []  # Temporary miscellaneous inventory list (used for switching items)
        self.__questionAsked: bool = False  # Flag indicating if a question has been asked to the player
        self.__textHistoryFile: str = "files/databases/textHistory.txt"  # Path to the text history file
        self.__stackedWidget: QStackedWidget = QStackedWidget() # Widget used to manage different screens
        self.__ui: Ui_StackedWidget = Ui_StackedWidget()  # UI object
        self.__lines: list[str] = []  # List of lines read from the text history file
        

        # UI setup
        self.__ui.setupUi(self.__stackedWidget)
        self.setCentralWidget(self.__stackedWidget)
        self.__stackedWidget.setCurrentIndex(0)
        
        self.__equipment_buttons: list[QPushButton] = [self.__ui.IButton1, self.__ui.IButton2, self.__ui.IButton3, self.__ui.IButton4, self.__ui.IButton5,
            self.__ui.IButton6, self.__ui.IButton7, self.__ui.IButton8, self.__ui.IButton9, self.__ui.IButton10,
            self.__ui.IButton11, self.__ui.IButton12, self.__ui.IButton13, self.__ui.IButton14, self.__ui.IButton15,
            self.__ui.IButton16, self.__ui.IButton17, self.__ui.IButton18, self.__ui.IButton19, self.__ui.IButton20,
            self.__ui.IButton22, self.__ui.IButton23, self.__ui.IButton24, self.__ui.IButton25, self.__ui.IButton26,
            self.__ui.IButton27, self.__ui.IButton28]  # List of buttons representing equipment slots

        # Connect buttons to methods
        self.__ui.inventoryButton.clicked.connect(self.__showInventory)
        self.__ui.mapButton.clicked.connect(self.__showMap)
        self.__ui.statusButton.clicked.connect(self.__showStatus)
        self.__ui.closeButton.clicked.connect(self.__showMain)
        self.__ui.closeButton_2.clicked.connect(self.__showMain)
        self.__ui.closeButton_3.clicked.connect(self.__showMain)
        self.__ui.submitInputButton.clicked.connect(self.__submitInput)

        # Set map image
        map = QPixmap("files/images/map.jpeg")
        self.__ui.mapPlaceholder.setPixmap(map)

        # Connect inventory change buttons to methods
        self.__ui.inventoryChangeEButton.clicked.connect(lambda: self.__changeToI(self.__tempEquInv))
        self.__ui.inventoryChangeCButton.clicked.connect(lambda: self.__changeToI(self.__tempConInv))
        self.__ui.inventoryChangeMButton.clicked.connect(lambda: self.__changeToI(self.__tempMiscInv))

        # Read text history file
        with open(self.__textHistoryFile, "r") as file:
            self.__lines = file.readlines()

        # Check if there is any text in history file
        if len(self.__lines) <= 0:
            self.__introText()  # Show intro text if no previous history
            self.ask_question("Embrace your destiny and choose your path: Fighter (1), Rogue (2), Wizard (3) - Type the corresponding number to embark on your adventure:", ["1", "2", "3"])
            self.__typingEffectTimer(40, 4)  # Add typing effect
            self.__traveling = True
        else:
            self.__addToOutputWithoutTypingEffect(self.__textHistoryFile, 0)  # Load previous text without typing effect
            self.__loadPlayer()  # Load player data
            self.__traveling = True

                  
    def __showInventory(self):
        """
        Shows the player's inventory.
        """

        self.__stackedWidget.setCurrentIndex(1)  # Switch to inventory screen

        # Clear temporary inventory lists
        self.__tempEquInv = []
        self.__tempConInv = []
        self.__tempMiscInv = []

        # Populate temporary lists based on item type
        for item in self.__player.get_items():
            if item.get_type() == "Equipment":
                self.__tempEquInv.append(item)
            elif item.get_type() == "Consumables":
                self.__tempConInv.append(item)
            else:
                self.__tempMiscInv.append(item)

        # Display equipment inventory by default
        self.__changeToI(self.__tempEquInv)               

    def __changeToI(self, Ilist: [Item]):
        """
        Updates the inventory display with the provided item list.
        """

        self.__resetInventory()  # Clear existing inventory text

        # Loop through items and set button text
        for i, item in enumerate(Ilist):
            if i < len(self.__equipment_buttons):  # Check if within button list bounds
                self.__equipment_buttons[i].setText(f"{item.get_item_name()} x{item.get_quantity()}")

            
    def __resetInventory(self):
        """
        Resets the inventory screen to its default state.
        """

        for i in range(len(self.__equipment_buttons)):
            self.__equipment_buttons[i].setText(f"S{i + 1}")  # Set buttons to default text

                        
    def __showMap(self):
        """
        Shows the map screen.
        """

        self.__stackedWidget.setCurrentIndex(2)

    def __showStatus(self):
        """
        Shows the player's status information.
        """

        self.__stackedWidget.setCurrentIndex(3)  # Switch to status screen

        self.__ui.statusMenu.clear()  # Clear previous text

        # Format player stats
        player_info = f"Archetype: {self.__player.get_archetype()}\n"
        mana_info = f"Mana: {self.__player.get_mana()} / {self.__player.get_max_mana()}\n"
        health_info = f"Health: {self.__player.get_health()} / {self.__player.get_max_health()}\n"
        stamina_info = f"Stamina: {self.__player.get_stamina()} / {self.__player.get_max_stamina()}\n"
        strength_info = f"Strength: {self.__player.get_strength()}\n"
        intelligence_info = f"Intelligence: {self.__player.get_intelligence()}\n"
        agility_info = f"Agility: {self.__player.get_agility()}\n"

        # Combine and display player information
        self.__ui.statusMenu.setText(player_info + mana_info + health_info + stamina_info + strength_info +
                                    intelligence_info + agility_info)
            
    def __showMain(self):
        """
        Shows the main screen.
        """

        self.__stackedWidget.setCurrentIndex(0)
  
    def __submitInput(self):
        """
        Submits the player's input and triggers the next question or action.
        """

        self.ask_question(self.__curQuestion, self.__curChoices)

      
    def ask_question(self, question: str, expected_answers: [str]):
        """
        Asks the player a question and stores their answer.
        """

        if not self.__questionAsked:
            # Add question to text history
            self.__addToHistory(self.__textHistoryFile, question)
            self.__curQuestion = question
            self.__curChoices = expected_answers
            self.__questionAsked = True
        else:
            answer = self.__ui.InputText.text()  # Get player input

            if answer in expected_answers:  # Check if answer is valid
                # Add answer to text history
                self.__addToHistory(self.__textHistoryFile, answer)
                self.__ui.InputText.setText("")  # Clear input field
                self.__curQuestion = ""
                self.__curChoices = []
                self.__typingEffectTimer(40, 1)  # Display answer with typing effect
                self.process_answer(0, answer)  # Process player's answer
                self.__questionAsked = False
            else:
                self.__ui.InputText.setText("")  # Clear input field if answer is invalid
                          
    def process_answer(self, answer_type: int, answer: str):
        """
        Processes the player's answer based on its type.

        Args:
            answer_type: Integer representing the type of answer (0 for character creation, 1 for area selection).
            answer: String containing the player's chosen answer.
        """

        if answer_type == 0:
            # Character creation
            if answer == "1":  # Fighter
                self.__player.set_archetype("Fighter")
                self.__player.set_max_health(150)
                self.__player.set_max_mana(50)
                self.__player.set_strength(15)
                self.__player.set_intelligence(5)
                self.__player.add_item(Item("Iron Sword", 0, 5, 0, 0, 0, 0, 0, 0, 1, "Equipment"))
                self.__player.add_skill(Skill("Slash", 1.5, 0, 25, 0))
                self.__save_player()
                self.__travel()
            elif answer == "2":  # Rogue
                self.__player.set_archetype("Rogue")
                self.__player.set_max_health(100)
                self.__player.set_max_mana(75)
                self.__player.set_agility(15)
                self.__player.set_intelligence(7)
                self.__player.add_item(Item("Topaz Staff", 0, 5, 0, 0, 0, 0, 0, 0, 1, "Equipment"))
                self.__player.add_skill(Skill("Firball", 0, 1.5, 0, 25))
                self.__save_player()
                self.__travel()
            elif answer == "3":  # Wizard
                self.__player.set_archetype("Wizard")
                self.__player.set_max_health(75)
                self.__player.set_max_mana(150)
                self.__player.set_agility(7)
                self.__player.set_strength(5)
                self.__player.set_intelligence(15)
                self.__player.add_item(Item("Iron Dagger", 0, 5, 0, 0, 0, 0, 0, 0, 1, "Equipment"))
                self.__player.add_skill(Skill("Backslash", 1.2, 0, 10, 0))
                self.__save_player()
                self.__travel()
        elif answer_type == 1:
            # Area selection
            self.__curAreaId = int(answer)
            
    def __addToHistory(self, filename: str, text: str):
        """
        Appends text to the given text history file.

        Args:
            filename: The path to the text history file.
            text: The text to be appended.
        """

        with open(filename, "a") as output_file:
            output_file.write(f"{text}\n")
        
    def __typingEffectTimer(self, interval, lines):
        """
        Starts a timer to display the provided text with a typing effect.

        Args:
            interval: The time interval between characters in the typing effect.
            lines: The number of lines to display with the typing effect.
        """

        self.__timer = QTimer()
        self.__timer.setInterval(interval)
        self.__timer.timeout.connect(lambda: self.__addToOutputWithTypingEffect(self.__textHistoryFile, lines))
        self.__timer.start()
        
    def __addToOutputWithTypingEffect(self, filename: str, num_lines: int):
        """
        Displays the specified number of lines from the text history file with a typing effect.

        Args:
            filename: The path to the text history file.
            num_lines: The number of lines to display.
        """

        # Clear the output text field
        self.__ui.OutputText.clear()

        # Append text without typing effect first
        self.__addToOutputWithoutTypingEffect(filename, num_lines)

        # Open the text history file for reading
        with open(filename, "r") as file:
            lines = file.readlines()

        # Extract desired lines based on `num_lines`
        if num_lines <= len(lines):
            last_lines = lines[-num_lines:]
        else:
            last_lines = lines

        # Initialize variables for typing effect logic
        self.__output_lines = last_lines
        self.__output_index = 0
        self.__char_index = 0

        # Disable input field while typing effect is active
        self.__ui.InputText.setEnabled(False)

        def update_text():
            """
            Updates the displayed text with a typing effect.
            """

            # Check if all lines have been displayed
            if self.__output_index >= len(self.__output_lines):
                self.__timer.stop()
                self.__ui.InputText.setEnabled(True)
                return

            # Get the current line
            line = self.__output_lines[self.__output_index]

            # Check if all characters in the line have been displayed
            if self.__char_index >= len(line):
                self.__char_index = 0
                self.__output_index += 1
                self.__ui.OutputText.append("\n")
                return

            # Get the next character to display
            char = line[self.__char_index]

            # Add the character to the output text
            self.__ui.OutputText.insertPlainText(char)

            # Update character index for next iteration
            self.__char_index += 1

        # Connect the update_text function to the timer's timeout signal
        self.__timer.timeout.connect(update_text)

        # Start the timer to trigger update_text periodically
        self.__timer.start()

        
    def __addToOutputWithoutTypingEffect(self, filename: str, lines: int):
        """
        Adds the specified number of lines from the text history file to the output text field without a typing effect.

        Args:
            filename: The path to the text history file.
            lines: The number of lines to add.
        """

        with open(filename, "r") as file:
            # Read all lines from the file
            all_lines = file.readlines()

            # Determine the starting index based on the number of lines and total lines
            if len(all_lines) >= 10:
                start_index = -10 - lines
            elif lines == 0:
                start_index = 0
            else:
                start_index = -lines

            # Extract the desired lines
            output_lines = all_lines[start_index:]

            # Append each line to the output text field with a newline character
            for line in output_lines:
                self.__ui.OutputText.insertPlainText(line)
                self.__ui.OutputText.append("\n")

    
    def __introText(self):
        """
        Displays the game's intro text.
        """

        self.__addToHistory(self.__textHistoryFile,
                            "The Last Hearth Tavern hummed with activity as a storm raged outside. You, a traveler seeking adventure, sat at a corner table, nursing a tankard of ale.")
        self.__addToHistory(self.__textHistoryFile,
                            "A cloaked man entered, carrying a strange, glowing tablet. He offered the artifact to the tavern, and you, drawn by the allure of adventure, stepped forward. The man warned you of the tablet's power and disappeared into the night.")
        self.__addToHistory(self.__textHistoryFile,
                            "You stared down at the table and saw some words start to appear on the surface of the stone.")

    def __save_player(self):
        """
        Saves the player's data to various files.
        """

        # Save player stats
        with open("files/databases/characterData.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            player_stats = [
                self.__player.get_archetype(),
                self.__player.get_max_mana(),
                self.__player.get_mana(),
                self.__player.get_max_health(),
                self.__player.get_health(),
                self.__player.get_max_stamina(),
                self.__player.get_stamina(),
                self.__player.get_strength(),
                self.__player.get_intelligence(),
                self.__player.get_agility(),
            ]
            writer.writerow(player_stats)

        # Save player items
        with open("files/databases/characterItems.dat", "wb") as f:
            pickle.dump(self.__player.get_items(), f)

        # Save player skills
        with open("files/databases/characterSkills.dat", "wb") as f:
            pickle.dump(self.__player.get_skills(), f)

    def __load_player(self):
        """
        Loads the player's data from various files.
        """

        # Load player stats from CSV file
        with open("files/databases/characterData.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            line = next(reader)
            self.__player.set_archetype(line[0])
            self.__player.set_max_mana(int(line[1]))
            self.__player.set_mana(int(line[2]))
            self.__player.set_max_health(int(line[3]))
            self.__player.set_health(int(line[4]))
            self.__player.set_max_stamina(int(line[5]))
            self.__player.set_stamina(int(line[6]))
            self.__player.set_strength(int(line[7]))
            self.__player.set_intelligence(int(line[8]))
            self.__player.set_agility(int(line[9]))

        # Load player items from binary file
        with open("files/databases/characterItems.dat", "rb") as f:
            items = pickle.load(f)
            for item in items:
                self.__player.add_item(item)

        # Load player skills from binary file
        with open("files/databases/characterSkills.dat", "rb") as f:
            skills = pickle.load(f)
            for skill in skills:
                self.__player.add_skill(skill)

    def __travel(self):
        """
        Loads and processes area information based on the player's current location.
        """

        self.__loaded_paths = []
        with open("files/databases/path.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.__loaded_paths.append(row)

        # Loop until the player stops traveling
        while self.__traveling:
            # Skip processing if player is in starting area
            if self.__curAreaId == 0:
                pass
            else:
                # Get area text and choices from loaded data
                text = self.__loaded_paths[self.__curAreaId - 1][0]
                choices = self.__loaded_paths[self.__curAreaId - 1][1:]

                # Add area text to history and ask player for input
                self.__addToHistory(self.__textHistoryFile, text)
                self.ask_question(text, choices)

                # Display text with typing effect and stop travel loop
                self.__typingEffectTimer(40, 1)
                self.__traveling = False