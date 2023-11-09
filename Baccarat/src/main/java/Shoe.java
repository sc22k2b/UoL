// TODO: Implement the Shoe class in this file

import java.util.Collections;

public class Shoe extends CardCollection {

    public Shoe(int decks) {

        if (!(decks == 6 || decks == 8)) {
            throw new CardException("Incorrect number of decks");
        }

        for (int i = 0; i < decks; i++) {
            for (Card.Suit suit : Card.Suit.values()) {
                for (Card.Rank rank : Card.Rank.values()) {
                    Card tempCard = new Card(rank, suit);
                    super.add(tempCard);
                }
            }
        }
    }

    public int size() {

        return super.size();
    }

    public void shuffle() {

        Collections.shuffle(cards);

    }

    public Card deal() {

        if (super.isEmpty()) {
            throw new CardException("Cannot deal from empty shoe");
        }

        Card removeCard = cards.remove(0);

        BaccaratCard bCard = new BaccaratCard(removeCard.getRank(), removeCard.getSuit());

        return bCard;
    }
}