package dk.cphbusiness.soft.mergesorttrouble;

import java.util.Random;

public class App {

    public static void main( String[] args ) {

        //== create and fill array
        int max = 2000_000;
        int[] arr = new int[ max ];
        Random ran = new Random();
        for ( int i = 0; i < arr.length; i++ ) {
            arr[ i ] = ran.nextInt( max * 10 );
        }

        //== Timing =============
        long startTime = System.nanoTime();

        MergeSort.merge_sort_start(arr);
        //Quicksort.quicksort( arr );
        //MergeSortLinkedLists.merge_sort_start(arr);
        //MergeSortCircularArrayLists.merge_sort_start(arr);
        long timeElapsed = System.nanoTime() - startTime;
        //=========================

        // print 20 first
        for ( int i = 0; i < 19; i++ ) {
            System.out.print( arr[ i ] + ", " );
        }
        System.out.println( arr[ 19 ] + ", ..." );

        System.out.println( "Time elapsed (millisec): " + timeElapsed / 1_000_000 );
    }

}
