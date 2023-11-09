// TODO: Implement the BaccaratCard class in this file

public class BaccaratCard extends Card {

    public BaccaratCard(Rank r, Suit s) {

        super(r, s); // Uses the constuctor from the super class Card

    }

    public Rank getRank() {

        return super.getRank(); // Uses the getRank() method from the super class Card
    }

    public Suit getSuit() {

        return super.getSuit(); // Uses the getSuit() method from the super class Card
    }

    public String toString() {

        return super.toString(); // Uses the toString() method from the super class Card
    }

    public boolean equals(Object other) {

        return super.equals(other); // Uses the equals() method from the super class Card
    }

    public int compareTo(Card other) {

        return super.compareTo(other); // Uses the compareTo() method from the super class Card
    }

    public int value() {

        int value = super.value(); // Uses the value() method from the super class Card

        if (value == 10) {
            return 0; // Changes any face card value to 0
        } else {
            return value;
        }
    }

}
