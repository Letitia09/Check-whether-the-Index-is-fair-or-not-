# Count-the-number-of-fair-indexes-
For given two arrays, split the arrays to some index k and find the sum of the subarrays. Index is said to be fair, only when the sum of each subarray are equal.<br>

You are given two arrays A and B consisting of N integers each.<br>

Index K is named fair if the four sums (A[0]+. +A[K-1]). (A[K]+...+A[N-1]). (B[0]+...+ B[K-1]) and (B[K] + ... + BIN-1]) are all equal. In other words, K is the index where the two arrays, A and B, can be split (into two non-empty arrays each) in such a way that the sums of the resulting arrays' elements are equal. <br>

For example, given arrays A=[0,4,-1,0,3], and B = [0, -2, 5,0,3], index K-3 is fair.<br>
The sums of the four subarrays are all equal: (0+4+(-1))=3; 0+3=3; 0+(-2)+5=3 and 0+3=3. On the other hand, Index K-2 is not fair, the sums of the subarrays <br>
Examples:

1. Given A = [0, 4, -1, 0, 3] and B = [0, -2, 5, 0, 3], your function should return 2. The fair indexes are 3 and 4. In both cases, the sums of elements of the subarrays are equal to 3. <br>

2. Given A = [2, -2, -3, 3] and B = [0, 0, 4, -4], your function should return 1. The only fair index is 2. Index 4 is not fair as the subarrays containing indexes from K to N-1 would be empty.<br>

3. Given A = [4,-1, 0, 3] and B = 1-2, 6, 0, 4], your function should return 0.

There are no fair indexes.<br>

4. Given A= [3, 2, 6] and B = [4, 1, 6], your function should return 0.<br>

5. Given A = [1, 4, 2, -2, 5], B = [7, -2, -2, 2, 5], your function should return 2. The

fair indexes are 2 and 4. <br>

