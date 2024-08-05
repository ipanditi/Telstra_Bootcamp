// Define the Game interface with abstract methods
interface Games {
    void startGame();
    void stopGame();
    void checkScore();
    void declareWinner();
}

// Implement OnlineGame class
class OnlineGame implements Games {
    @Override
    public void startGame() {
        System.out.println("Start online game");
    }

    @Override
    public void stopGame() {
        System.out.println("Stop online game");
    }

    @Override
    public void declareWinner() {
        System.out.println("The online winner");
    }

    @Override
    public void checkScore() {
        System.out.println("Checked");
    }

    public void platform() {
        System.out.println("Online platform");
    }
}

// Implement OfflineGame class
class OfflineGame implements Games {
    @Override
    public void startGame() {
        System.out.println("Start offline game");
    }

    @Override
    public void stopGame() {
        System.out.println("Stop offline game");
    }

    @Override
    public void declareWinner() {
        System.out.println("The offline winner");
    }

    @Override
    public void checkScore() {
        System.out.println("Score checked");
    }

    public void sport() {
        System.out.println("Sport");
    }
}

// Implement SinglePlayer class extending OnlineGame
class SinglePlayer extends OnlineGame {
    public void openWorld() {
        System.out.println("GTA");
    }
}

// Implement MultiPlayer class extending OnlineGame
class MultiPlayer extends OnlineGame {
    public void shooting() {
        System.out.println("CS GO");
    }
}

// Implement Indoor class extending OfflineGame
class Indoor extends OfflineGame {
    public void court() {
        System.out.println("Playing in an indoor court");
    }
}

// Implement Outdoor class extending OfflineGame
class Outdoor extends OfflineGame {
    public void ground() {
        System.out.println("Playing on a ground");
    }
}

// Main class to test the implementation
public class Game {
    public static void main(String args[]) {
        Outdoor vivek = new Outdoor();
        vivek.checkScore();  // This will print "Score checked"
    }
}


