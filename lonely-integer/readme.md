You will be given an array of integers. All of the integers except one occur twice. That one is unique in the array.

Given an array of integers, find and print the unique element.

**Input Format**

The first line contains a single integer, , denoting the number of integers in the array. 
The second line contains  space-separated integers describing the respective values in .

**Constraints**

* `1 <= n < 100`
* It is guaranteed that `n` is an odd number and that there is one unique element.
* `0 <= a^i <= 100`, where `0 <= i < n`.

**Output Format**

Print the unique integer in the array.

**Sample Input 0**

```
1
1
```

**Sample Output 0**

```
1
```

**Explanation 0**

There is only one element in the array, thus it is unique.

**Sample Input 1**

```
3
1 1 2
```

**Sample Output 1**

```
2
```

**Explanation 1**

We have two 's, and  is unique.

**Sample Input 2**

```
5
0 0 1 2 1
```

**Sample Output 2**

```
2
```

**Explanation 2**

We have two 's, two 's, and one .  is unique.