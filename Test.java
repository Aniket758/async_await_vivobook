import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        System.out.println();
        // static int fun(){
        // static int x=0;
        // return ++x;
        // }

    }

    public static long getMin(List<Integer> price, int k) {
        Collections.sort(price);
        int n = price.size();
        int medianIndex;
        medianIndex = n % 2 == 0 ? ((n) / 2) : (n + 1) / 2;
        System.out.println("----" + medianIndex);
        int median = price.get(medianIndex - 1);
        int c = 0;

        if (median < k)
            while (true) {
                if (price.get(medianIndex) - price.get(medianIndex - 1) >= k) {

                    break;
                }
                c++;
                medianIndex++;
            }
        else {
            while (true) {
                if (price.get(medianIndex - 1) - price.get(medianIndex - 2) >= k) {

                    break;
                }
                c++;
                medianIndex--;
            }
        }
        System.err.println("---" + median);
        long moves = Math.abs(median - k);
        // System.err.println("moves"+moves);
        moves = moves + c;
        return moves;
    }
}