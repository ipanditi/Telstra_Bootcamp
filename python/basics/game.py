from abc import ABC, abstractmethod
class Game(ABC):
    @abstractmethod
    def startGame(self):
        pass

    @abstractmethod
    def stopGame(self):
        pass
    
    @abstractmethod
    def checkScore(self):
        pass
    
    @abstractmethod
    def declareWinner(self):
        pass
    
class OnlineGame(Game):
    def startGame(self):
        print("Start online game")
    
    def stopGame(self):
        print("Stop online game")
    
    def declareWinner(self):
        print("The online winner")
        
    def checkScore(self):
        print("Checked")
    
    def platform(self):
        print("Online platform")

class OfflineGame(Game):
    def startGame(self):
        print("Start offline game")
    
    def stopGame(self):
        print("Stop offline game")
    
    def declareWinner(self):
        print("The offline winner")
    
    def checkScore(self):
        print("score checked")
    
    def sport(self):
        print("Sport")

class SinglePlayer(OnlineGame):
    def openworld(self):
        print("GTA")
    
class MultiPlayer(OnlineGame):
    def shooting(self):
        print("CS GO")
        
class Indoor(OfflineGame):
    def court(self):
        print("Playing in an indoor court")

class Outdoor(OfflineGame):
    def ground(self):
        print("Playing on a ground")
    
vivek = Outdoor()
vivek.checkScore()