// TODO: Implement the BaccaratHand class in the file

public class BaccaratHand extends CardCollection {

    public BaccaratHand() {
        super(); //Uses the constructor from the superclass CardCollection
    }

    public int size() {

        return super.size(); //Uses the size() method from the super class
    }

    public void add(Card card) {

        super.add(card); //Uses the add method from the super class

    }

    @Override
    public int value() {

        int sum = 0;
        //Loops for the number of cards and combines their value
        for (Card card : cards) {
            if (card.value() == 10) {
                return 1;
            } else {
                sum += card.value();
            }
        }
        if (sum > 9) {
            return sum - 10;
        } else {
            return sum;
        }
    }

    public boolean isNatural() {

        if (size() == 2) {
            if (value() == 8 || value() == 9) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    public String toString() {

        String tempString = "";
        int count = 0;

        for (Card card : cards) {
            count++;
            tempString = tempString + card.getRank().getSymbol() + card.getSuit().getSymbol();
            if (count != cards.size()) {
                tempString = tempString + " ";
            }
        }

        return tempString;
    }
}
