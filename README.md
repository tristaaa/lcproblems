# leetcode problems

[| Sum problems](https://github.com/tristaaa/lcproblems/blob/master/README.md#-sum-problems)<br>
&ensp;&ensp;[- Two Sum](https://github.com/tristaaa/lcproblems/blob/master/README.md#11-two-sum)<br>
&ensp;&ensp;[- Three Sum](https://github.com/tristaaa/lcproblems/blob/master/README.md#12-three-sum)<br>
&ensp;&ensp;[- Four Sum](https://github.com/tristaaa/lcproblems/blob/master/README.md#13-four-sum)<br>

---

## | Sum problems
### 1.1 Two Sum
#### -basic
 - Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 - You may assume that each input would have exactly one solution, and you may not use the same element twice.
 - **Example:**
    ```python
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    ```
 - [twosum](https://github.com/tristaaa/lcproblems/blob/master/twosum.py)

#### -two sum - input array sorted
 - Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
 - The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
 - Note: 
  - Your returned answers (both index1 and index2) are not zero-based.
  - You may assume that each input would have exactly one solution and you may not use the same element twice.
 -  **Example:**
    ```python
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    ```
 - [twosumII](https://github.com/tristaaa/lcproblems/blob/master/twosumii.py)

#### -two sum - input is a binary search tree
 - Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
 - The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
 - Note: 
  - Your returned answers (both index1 and index2) are not zero-based.
  - You may assume that each input would have exactly one solution and you may not use the same element twice.
 -  **Example:**
    ```python
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    ```
 - [twosumIV](https://github.com/tristaaa/lcproblems/blob/master/twosumii.py)



### 1.2 Three Sum
 - Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
 - Find all unique triplets in the array which gives the sum of zero.
 - Note: The solution set must not contain duplicate triplets.
 - **Example:**
    ```python
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    ```
 - [threesum](https://github.com/tristaaa/lcproblems/blob/master/threesum.py)

### 1.3 Four Sum
#### -basic
 - Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
 - Find all unique quadruplets in the array which gives the sum of target.
 - Note: The solution set must not contain duplicate quadruplets.
 - **Example:**
    ```python
    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
    ```
 - [foursum](https://github.com/tristaaa/lcproblems/blob/master/foursum.py)
    - a general solution for all numbers of N sum using two pointers

#### -four sum count
 - Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
 - To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
 - **Example:**
    ```python
    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]

    Output:
    2

    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
    ```
 - [foursumcount](https://github.com/tristaaa/lcproblems/blob/master/foursumcount.py)






