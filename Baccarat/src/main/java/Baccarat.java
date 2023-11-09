import java.util.NoSuchElementException;
import java.util.Scanner;

public class Baccarat {
    // TODO: Implement your Baccarat simulation program here

    public static void main(String args[]) {

        // Setting up of the objects to be used and the game as well as shuffling the
        // shoe and deciding if the game is to be played interactivley or not

        boolean automatic = true;

        if(args.length != 0){

            if(args[0].equals("-i") || args[0].equals("--interact")){

                automatic = false;
            }
        }

        Baccarat game = new Baccarat();

        Shoe gameShoe = new Shoe(6);

        gameShoe.shuffle();

        BaccaratHand bankerHand = new BaccaratHand();

        BaccaratHand playerHand = new BaccaratHand();

        System.out.println("Round 1");

        game.gameSetup(gameShoe, playerHand, bankerHand);

        game.gameContinuation(gameShoe, playerHand, bankerHand, automatic);

    }

    public int gameSetup(Shoe gameShoe, BaccaratHand playerHand, BaccaratHand bankerHand) {

        // Deals the player and banker 2 cards each
        playerHand.add(gameShoe.deal());
        bankerHand.add(gameShoe.deal());

        playerHand.add(gameShoe.deal());
        bankerHand.add(gameShoe.deal());

        displayValues(playerHand, bankerHand);

        // Identifies if either the player or banker has a natural
        if (playerHand.isNatural()) {
            System.out.println("Player has a Natural");
            return 1;
        } else if (bankerHand.isNatural()) {
            System.out.println("Banker has a Natural");
            return 2;
        } else {
            return 100;
        }

    }

    public void gameContinuation(Shoe gameShoe, BaccaratHand playerHand, BaccaratHand bankerHand, boolean automatic) {

        boolean nextRound = true;
        int playerWins = 0;
        int bankerWins = 0;
        int ties = 0;
        int numberOfGames = 0;
        int naturalHolder = 100;

        /*
         * NATURAL HOLDER DEFINITIONS
         * 1 == Player is the natural holder
         * 2 == Banker is the natural holder
         * 100 (Any other number) == There is no current natural holder
         */

        // Loops through the game whilst the player still wants another round and there
        // are enough cards left
        while (nextRound == true) {

            if (numberOfGames > 0) {

                // Resets the hands (as they will already have cards in them from the previous
                // round)
                playerHand.discard();
                bankerHand.discard();
                System.out.println("Round " + numberOfGames);
                naturalHolder = gameSetup(gameShoe, playerHand, bankerHand);

                // Checks to see if the new hand is a natural
                if (naturalHolder == 1) {
                    playerWins = playerWins + 1;
                } else if (naturalHolder == 2) {
                    bankerWins = bankerWins + 1;
                }

            }

            // Continues the game if the natural holder
            if (naturalHolder == 100) {
                playerRule(gameShoe, playerHand); // Consults the rule for the players hand (win or not/deal third card)

                bankerRule(gameShoe, playerHand, bankerHand); // Consults the rule for the bankers hand (win or not/deal
                                                              // third card)

                displayValues(playerHand, bankerHand);

                int gameResult = resultDecider(playerHand, bankerHand);

                // Identifies what the outcome of the game was
                if (gameResult == 1) {
                    playerWins = playerWins + 1;
                } else if (gameResult == 2) {
                    bankerWins = bankerWins + 1;
                } else {
                    ties = ties + 1;
                }

                if(numberOfGames == 0){
                    numberOfGames++;
                }
            }

            if (gameShoe.size() < 6) {
                break; // Stops the game as there are not enough cards in the shoe to continue playing
            }

            if(automatic == true){
                nextRound = true;
            }
            else{
                nextRound = continueGame();
            }

            naturalHolder = 100;

            numberOfGames++;

        }

        // Displays to the user the end of game stats
        System.out.println("\n");
        System.out.println(numberOfGames + " rounds played");
        System.out.println(playerWins + " player wins");
        System.out.println(bankerWins + " banker wins");
        System.out.println(ties + " ties");

        System.exit(0);
    }

    public void playerRule(Shoe gameShoe, BaccaratHand playerHand) {

        // Identifies if the player requires a third card
        if (playerHand.value() < 6) {
            System.out.println("Dealing third card to player...");
            Card thirdCard = gameShoe.deal();
            playerHand.add(thirdCard);
        }
    }

    public void bankerRule(Shoe gameShoe, BaccaratHand playerHand, BaccaratHand bankerHand) {

        if (playerHand.size() == 2) {
            if (bankerHand.value() < 6) {
                dealBanker(gameShoe, bankerHand);
            }
        } else {
            int thirdCardValue = playerHand.cards.get(2).value();

            if (bankerHand.value() < 3) {
                dealBanker(gameShoe, bankerHand);
            } else if (bankerHand.value() == 3) {

                if (thirdCardValue != 8) {
                    dealBanker(gameShoe, bankerHand);
                }

            } else if (bankerHand.value() == 4) {

                if (thirdCardValue == 2 || thirdCardValue == 3 || thirdCardValue == 4 || thirdCardValue == 5
                        || thirdCardValue == 6 || thirdCardValue == 7) {
                    dealBanker(gameShoe, bankerHand);
                }
            } else if (bankerHand.value() == 5) {

                if (thirdCardValue == 4 || thirdCardValue == 5 || thirdCardValue == 6 || thirdCardValue == 7) {
                    dealBanker(gameShoe, bankerHand);
                }

            } else if (bankerHand.value() == 6) {

                if (thirdCardValue == 6 || thirdCardValue == 7) {
                    dealBanker(gameShoe, bankerHand);
                }
            }
        }
    }

    public void dealBanker(Shoe gameShoe, BaccaratHand bankerHand) {

        System.out.println("Dealing third card to banker...");
        bankerHand.add(gameShoe.deal());
    }

    public void displayValues(BaccaratHand playerHand, BaccaratHand bankerHand) {

        System.out.println("Player: " + playerHand.toString() + " = " + playerHand.value());
        System.out.println("Banker: " + bankerHand.toString() + " = " + bankerHand.value());

    }

    public int resultDecider(BaccaratHand playerHand, BaccaratHand bankerHand) {

        if (playerHand.value() > bankerHand.value()) {
            System.out.println("Player win!");
            return 1;
        }
        if (playerHand.value() < bankerHand.value()) {
            System.out.println("Banker win!");
            return 2;
        } else {
            System.out.println("Tie");
            return 0;
        }
    }

    public boolean continueGame() {

        Scanner userInput = new Scanner(System.in);
        System.out.println("Another round? (y/n): ");

        System.out.println('\n');

        try {

            String gameChoice = userInput.nextLine();

            if (gameChoice.toUpperCase().charAt(0) == 'Y') {
                return true;
            } else {
                return false;
            }
        } catch (NoSuchElementException e) {
            return true;
        }

    }

}
