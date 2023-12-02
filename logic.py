from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui import *
from pynput.keyboard import *
from character import *

class gameLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__player = Character()
        self.__curQuestion= ''
        self.__curChoices = []
        self.__questionAsked = False
        self.__textHistoryFile = 'files/databases/textHistory.txt'
        self.__stackedWidget = QStackedWidget()
        self.__ui = Ui_StackedWidget()
        self.__ui.setupUi(self.__stackedWidget)
        self.setCentralWidget(self.__stackedWidget)
        self.__stackedWidget.setCurrentIndex(0)
        self.__ui.inventoryButton.clicked.connect(self.__showInventory)
        self.__ui.mapButton.clicked.connect(self.__showMap)
        self.__ui.statusButton.clicked.connect(self.__showStatus)
        self.__ui.closeButton.clicked.connect(self.__showMain)
        self.__ui.closeButton_2.clicked.connect(self.__showMain)
        self.__ui.closeButton_3.clicked.connect(self.__showMain)
        self.__ui.saveButton.clicked.connect(self.__saveButton)
        self.__ui.submitInputButton.clicked.connect(self.__submitInput)
        map = QPixmap('files/images/map.jpeg')
        self.__ui.mapPlaceholder.setPixmap(map)
        
        
        
        with open(self.__textHistoryFile, 'r') as file:
          self.__lines = file.readlines()
          
          if len(self.__lines) <= 0:
            self.__introText()  
            self.ask_question("Embrace your destiny and choose your path: Fighter (1), Rogue (2), Wizard (3) - Type the corresponding number to embark on your adventure:", ['1','2','3'])
            self.__typingEffectTimer(40, 4)
                  
    def __showInventory(self):
        self.__stackedWidget.setCurrentIndex(1)

    def __showMap(self):
        self.__stackedWidget.setCurrentIndex(2)

    def __showStatus(self):
        self.__stackedWidget.setCurrentIndex(3)
        self.__ui.statusMenu.clear()
        self.__ui.statusMenu.setText(f"Archetype: {self.__player.get_archetype()}\n"
                                f"Mana: {self.__player.get_mana()} / {self.__player.get_max_mana()}\n"
                                f"Health: {self.__player.get_health()} / {self.__player.get_max_health()}\n"
                                f"Stamina: {self.__player.get_stamina()} / {self.__player.get_max_stamina()}\n"
                                f"Strength: {self.__player.get_strength()}\n"
                                f"Intelligence: {self.__player.get_intelligence()}\n"
                                f"Agility: {self.__player.get_agility()}")
        
    def __showMain(self):
        self.__stackedWidget.setCurrentIndex(0)
    
    def __saveButton(self):
        pass
      
    def __submitInput(self):
        self.ask_question(self.__curQuestion, self.__curChoices)
      
    def ask_question(self, question, expected_answers):
        if self.__questionAsked == False:
            self.__addToHistory(self.__textHistoryFile, question)
            self.__curQuestion = question
            self.__curChoices = expected_answers
            self.__questionAsked = True
        else: 
            __answer = self.__ui.InputText.text()
            if __answer in expected_answers:
                self.__addToHistory(self.__textHistoryFile, __answer)
                self.__ui.InputText.setText('')
                self.__curQuestion = ''
                self.__curChoices = []
                self.__typingEffectTimer(40, 1)
                self.processAnswer(0, __answer)
                self.__questionAsked = False
            else:
                self.__ui.InputText.setText('')
                          
    def processAnswer(self, type, answer):
        if type == 0:
            if answer == '1':
                self.__player.set_archetype('Fighter')
                self.__player.set_max_health(150)
                self.__player.set_max_mana(50)
                self.__player.set_strength(15)
                self.__player.set_intelligence(5)
            elif answer == '2':
                self.__player.set_archetype('Rouge')
                self.__player.set_max_health(100)
                self.__player.set_max_mana(75)
                self.__player.set_agility(15)
                self.__player.set_intelligence(7)
            elif answer =='3':
                self.__player.set_archetype('Wizard')
                self.__player.set_max_health(75)
                self.__player.set_max_mana(150)
                self.__player.set_agility(7)
                self.__player.set_strength(5)
                self.__player.set_intelligence(15)
            
    def __addToHistory(self, filename, text):
      __output_file = open(filename, 'a')
      __output_file.write(text + '\n')
      
    def __typingEffectTimer(self, interval, lines):
      self.__timer = QTimer()
      self.__timer.setInterval(interval)
      self.__timer.timeout.connect(lambda: self.__addToOutputWithTypingEffect(self.__textHistoryFile, lines))
      self.__timer.start()
      
    def __addToOutputWithTypingEffect(self, filename, num_lines):
        self.__ui.OutputText.clear()
        self.__addToOutputWithoutTypingEffect(self.__textHistoryFile, num_lines)

        with open(filename, 'r') as file:
            lines = file.readlines()

            if num_lines <= len(lines):
                last_lines = lines[-num_lines:]
            else:
                last_lines = lines

        self.__output_lines = last_lines
        self.__output_index = 0
        self.__char_index = 0

        self.__ui.InputText.setEnabled(False)

        def update_text():
          if self.__output_index >= len(self.__output_lines):
              self.__timer.stop()
              self.__ui.InputText.setEnabled(True)
              return

          line = self.__output_lines[self.__output_index]

          if self.__char_index >= len(line):
              self.__char_index = 0
              self.__output_index += 1
              self.__ui.OutputText.append('\n')
              return

          char = line[self.__char_index]
          self.__ui.OutputText.insertPlainText(char)
          self.__char_index += 1

        self.__timer.timeout.connect(update_text)
        self.__timer.start()
        
    def __addToOutputWithoutTypingEffect(self, filename, line):
        with open(filename, 'r') as file:
            __lines = file.readlines()

            if len(__lines) >= 10:
                __last_lines = __lines[-10: -line]
            else:
                __last_lines = __lines[:-line]

        for line in __last_lines:
            self.__ui.OutputText.insertPlainText(line)
            self.__ui.OutputText.append('\n')   
    
    def __introText(self):
      self.__addToHistory(self.__textHistoryFile, "The Last Hearth Tavern hummed with activity as a storm raged outside. You, a traveler seeking adventure, sat at a corner table, nursing a tankard of ale. A cloaked man entered, carrying a strange, glowing tablet.")
      self.__addToHistory(self.__textHistoryFile, "He offered the artifact to the tavern, and you, drawn by the allure of adventure, stepped forward. The man warned you of the tablet's power and disappeared into the night.")
      self.__addToHistory(self.__textHistoryFile, "You stared down at the table and saw some words start to appear of the surface of the stone.")
      