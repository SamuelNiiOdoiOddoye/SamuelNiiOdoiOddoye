package JavaBasics;

public class FibonnacciNumber {

    public static void main(String[] args){

/*
 * 
 1.	Fibonacci Number
Write a method that returns the nth element of the Fibonacci Sequence
The Fibonacci Sequence is the series of numbers: 0,1,1,2,3,5,8,13,21,34,…
The next number is found by adding up the two numbers before it

 * 
 */
        System.out.println(fibonacci(25));

    }

    public static Integer fibonacci(Integer n){

    }
public Integer fibonnaci(Integer n) {
    if (n == 1) {
        return 1;
    }else if ( n==0 ) {
        return 0;
    }else {
        return fibonnaci(n-1) + fibonnaci( n - 2 );
    }
    
}

}

