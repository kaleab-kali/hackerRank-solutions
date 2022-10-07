**Sorting: Bubble Sort ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.001.png) ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.002.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.003.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.004.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.005.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.006.png)**

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.007.png)

`    `for (int j = 0; j < n - 1; j++) {

`        `// Swap adjacent elements if they are in decreasing order         if (a[j] > a[j + 1]) {

`            `swap(a[j], a[j + 1]);

`        `}

`    `}

}

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

1. Array is sorted in numSwaps swaps. , where  is the number of swaps that took place.![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.008.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.009.png)
1. First Element: firstElement , where  is the first element in the sorted array.![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.010.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.011.png)
1. Last Element: lastElement , where  is the last element in the sorted array.![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.012.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.013.png)

**Hint:** To complete this challenge, you must add a variable that keeps a running tally of  all swaps that occur during execution.

For example, given a worst-case but small array to sort:  we go through the following steps:![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.014.png)

swap    a       0       ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.015.png)[6,4,1] 1       [4,6,1] 2       [4,1,6] 3       [1,4,6]

It took  swaps to sort the array. Output would be![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.016.png)

Array is sorted in 3 swaps.  ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.017.png)First Element: 1  

Last Element: 6  

**Function Description**

Complete the function countSwaps in the editor below. It should print the three lines required, then return.

countSwaps has the following parameter(s):

![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.018.png) a: an array of integers .

**Input Format**

The first line contains an integer,  , the size of the array  . The ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.019.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.020.png)second line contains  space-separated integers  .![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.021.png)

**Constraints**

` `![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.022.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.023.png)

` `![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.024.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.025.png)

**Output Format**

You must print the following three lines of output:

1. Array is sorted in numSwaps swaps. , where  is the number of swaps that took place.![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.026.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.027.png)
1. First Element: firstElement , where  is the first element in the sorted array.![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.028.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.029.png)
1. Last Element: lastElement , where  is the last element in the sorted array.![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.030.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.031.png)

**Sample Input 0**

3![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.032.png)

1 2 3

**Sample Output 0**

Array is sorted in 0 swaps. ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.033.png)First Element: 1

Last Element: 3

**Explanation 0** 

The array is already sorted, so  swaps take place and we print the necessary three lines of output shown ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.034.png)above.

**Sample Input 1**

3![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.035.png)

3 2 1

**Sample Output 1**

Array is sorted in 3 swaps. ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.036.png)First Element: 1

Last Element: 3

**Explanation 1** 

The array is not sorted, and its initial values are:  . The following  swaps take place:![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.037.png)![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.038.png)

1. ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.039.png)
1. ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.040.png)
1. ![](Aspose.Words.1dd5eb76-2861-4a5c-a925-48c506cb40ec.041.png)

At this point the array is sorted and we print the necessary three lines of output shown above.
