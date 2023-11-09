public class rotate2{

    public static void main(String[] args)
    {
        int N = 8192;
        int D = 3;
        rotate(N, D);
    }
 
    static void rotate(int N, int D)
    {
        // your code here
        int t = 16;
        int left = ((N << D) | N >> (t - D)) & 0xFFFF;

        System.out.println("This the first option: " + (N << D));
        System.out.println("This is the second option: " + (N >> (t - D)));
        System.out.println("This is the third thing: " + ((N << D) | N >> (t - D)));

        System.out.println(left);
    }
    
     
}