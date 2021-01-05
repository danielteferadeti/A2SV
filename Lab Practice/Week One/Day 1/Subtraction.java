/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package a2sv;

/**
 *
 * @author Dani wiz Jesus
 */
public class A2SV {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        // int k;
        // k = numChar("3244");
        String k = "2147483647999";
        addStrings("199", "78");
        // System.out.println(12%10);

    }

    public static String strReverser(String toBeRev) {

        String input = toBeRev;

        // into bytes[].
        byte[] strAsByteArray = input.getBytes();

        byte[] result = new byte[strAsByteArray.length];

        // Store result in reverse order into the
        // result byte[]
        for (int i = 0; i < strAsByteArray.length; i++) {
            result[i] = strAsByteArray[strAsByteArray.length - i - 1];
        }

        return new String(result);
    }

    public static int numChar(String given) {

        String input = given;
        int totalNumCh = 0;

        byte[] strAsByteArray = input.getBytes();

        for (int i = 0; i < strAsByteArray.length; i++) {
            totalNumCh += 1;
        }
        return totalNumCh;
    }

    public static String addZero(String k, int dif) {

        String toReturn = k;

        for (int i = 0; i < dif; i++) {
            toReturn += "0";
        }
        return toReturn;
    }

    public static void addStrings(String numA, String numB) {

        // reversed and number of Char in A
        String revA = strReverser(numA);
        int charA = numChar(numA);

        // reversed and number of Char in B
        String revB = strReverser(numB);
        int charB = numChar(numB);

        String sumResult = "";
        int carry = 0;

        if (charA > charB) {
            int dif = charA - charB;
            revB = addZero(revB, dif);
        } else if (charB > charA) {
            int dif = charB - charA;
            revA = addZero(revA, dif);
        }

        for (int i = 0; i < revA.length(); i++) {
            int numOne = Integer.parseInt(String.valueOf(revA.charAt(i)));
            int numTwo = Integer.parseInt(String.valueOf(revB.charAt(i)));
            // System.out.println("AAAAAA----->" + numOne + " BBBBB ----> " + numTwo);

            int sum = numOne + numTwo + carry;
            if (sum > 9) {
                int notCarry = sum % 10;
                sumResult += notCarry;
                carry = 1;
            } else {
                sumResult += sum;
                carry = 0;
            }
            System.out.println("Current Sum ----->" + sumResult + "  Carry ---> " + carry);
        }
        System.out.println("SUM RESULT ----->" + strReverser(sumResult));
    }

    public static void subNum() {

    }

    public static void multString(String numA, String numB) {

    }

}