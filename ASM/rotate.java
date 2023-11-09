public class rotate{

    public static void main(String args[]){

        int maxNumber = 65535;
        int actualNumber = 8192;
        int numOfPlaces = 3;

        checkSize(numOfPlaces, maxNumber, actualNumber);

    }

    public static void checkSize(int numOfPlaces, int maxNumber, int actualNumber){

        int rightShift = maxNumber >> numOfPlaces;
        System.out.println("This is the right shift: " + rightShift);


        int result = rightShift - actualNumber;
        if(result>=0){
            System.out.println("This is the number: " + (actualNumber<<numOfPlaces));
        }
        else{
            int difference = actualNumber>>(16-numOfPlaces);

            System.out.println("This is the difference: " + difference);

            int rotatedNumber = ((actualNumber + result)<<numOfPlaces) + difference;

            System.out.println("This is the shifted number: " + ((actualNumber + result)<<numOfPlaces));

            System.out.println("This is the rotated number: " + rotatedNumber);


        }

    }
}