# leetcode problems

[| Sum problems](https://github.com/tristaaa/lcproblems/blob/master/README.md#-sum-problems)<br>
&ensp;&ensp;[- Two Sum](https://github.com/tristaaa/lcproblems/blob/master/README.md#11-two-sum)<br>
&ensp;&ensp;[- Three Sum](https://github.com/tristaaa/lcproblems/blob/master/README.md#12-three-sum)<br>
&ensp;&ensp;[- Four Sum](https://github.com/tristaaa/lcproblems/blob/master/README.md#13-four-sum)<br>
[| Stack problems](https://github.com/tristaaa/lcproblems/blob/master/README.md#-stack-problems)<br>
&ensp;&ensp;[- Binary Search Tree Iterator](https://github.com/tristaaa/lcproblems/blob/master/README.md#21-binary-search-tree-iterator)<br>
[| Add problems](https://github.com/tristaaa/lcproblems/blob/master/README.md#-add-problems)<br>
&ensp;&ensp;[- Add Two Numbers](https://github.com/tristaaa/lcproblems/blob/master/README.md#31-add-two-numbers)<br>
&ensp;&ensp;&ensp;&ensp;[- Basic (Linked List)](https://github.com/tristaaa/lcproblems/blob/master/README.md#-basic--form-of-linked-list)<br>
&ensp;&ensp;&ensp;&ensp;[- Not Reversed (Linked List)](https://github.com/tristaaa/lcproblems/blob/master/README.md#-form-of-linked-listnot-reversed-order)<br>
&ensp;&ensp;&ensp;&ensp;[- Add to Array](https://github.com/tristaaa/lcproblems/blob/master/README.md#-add-an-integer-to-an-array-form-of-integer)<br>
&ensp;&ensp;&ensp;&ensp;[- Add Binary Strings](https://github.com/tristaaa/lcproblems/blob/master/README.md#-add-two-binary-strings)<br>
&ensp;&ensp;&ensp;&ensp;[- Add Integer Strings](https://github.com/tristaaa/lcproblems/blob/master/README.md#-add-two-integer-strings)<br>
&ensp;&ensp;&ensp;&ensp;[- Add Integer Using Bit Manipulation](https://github.com/tristaaa/lcproblems/blob/master/README.md#-add-two-numbers-using-bit-manipulation)<br>
&ensp;&ensp;&ensp;&ensp;[- Multiply Integer Strings](https://github.com/tristaaa/lcproblems/blob/master/README.md#--multiply-integer-strings)<br>
[| Substring problems](https://github.com/tristaaa/lcproblems/blob/master/README.md#-substring-problems)<br>

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

#### -two sum - design a data structure
 - Design and implement a TwoSum class. It should support the following operations: `add` and `find`.
 - `add`: Add the number to an internal data structure.
 - `find`: Find if there exists any pair of numbers which sum is equal to the value.
 - **Example:**
    ```python
    add(1)
    add(3)
    add(5)
    find(4) # return True
    find(7) # return False
    ```
 - [twosumIII](https://github.com/tristaaa/lcproblems/blob/master/twosumiii.py)

#### -two sum - input is a binary search tree
 - Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
 -  **Example:**
    ```python
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    Output: True
    ```
 - [twosumIV](https://github.com/tristaaa/lcproblems/blob/master/twosumiv.py)


### 1.2 Three Sum
#### -basic
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
 - [3sum](https://github.com/tristaaa/lcproblems/blob/master/threesum.py)

#### -three sum closest
 - Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
 - Return the sum of the three integers. You may assume that each input would have exactly one solution.
 - **Example:**
    ```python
    Given array nums = [-1, 2, 1, -4], and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    ```
 - [3sumClosest](https://github.com/tristaaa/lcproblems/blob/master/threesumclosest.py)

#### -three sum smaller
 - Given an array of n integers `nums` and a target, find the number of index triplets `(i,j,k)` with `0<=i<j<k<n` that satisfy the condition: `nums[i]+nums[j]+nums[k] < target`.
 - **Example:**
    ```python
    Input: nums = [-2,0,1,3], and target = 2
    Output: 2
    Explanation: Because there are two triplets which sums are less than 2:
        [-2,0,1]
        [-2,0,3]
    ```
 - [3sumSmaller](https://github.com/tristaaa/lcproblems/blob/master/threesumsmaller.py)



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
 - [4sum](https://github.com/tristaaa/lcproblems/blob/master/foursum.py)
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
 - [4sumCount](https://github.com/tristaaa/lcproblems/blob/master/foursumcount.py)



## | Stack problems
### 2.1 Binary Search Tree Iterator
 - Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
 - Calling `next()` will return the next smallest number in the BST.
 - Note: 
  - `next()` and `hasNext()` should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
  - You may assume that `next()` call will always be valid, that is, there will be at least a next smallest number in the BST when `next()` is called.
 - **Example:**
    ```python
    Input: 
        7
       / \
      3   15
         /  \
        9   20

    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    # return 3
    iterator.next();    # return 7
    iterator.hasNext(); # return True
    iterator.next();    # return 9
    iterator.hasNext(); # return True
    iterator.next();    # return 15
    iterator.hasNext(); # return True
    iterator.next();    # return 20
    iterator.hasNext(); # return False
    ```
 - [bstIterator](https://github.com/tristaaa/lcproblems/blob/master/bstiter.py)



## | Add problems
### 3.1 Add Two Numbers
#### -basic -form of Linked List
 - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. 
 - Add the two numbers and return it as a linked list.
 - You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 - **Example:**
    ```python
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    ```
 - [addTwoNumbers](https://github.com/tristaaa/lcproblems/blob/master/addtwonum.py)

#### -form of Linked List(not reversed order)
 - You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 - You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 - Note: What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
 - **Example:**
    ```python
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
    ```
 - [addTwoNumbersII](https://github.com/tristaaa/lcproblems/blob/master/addtwonumii.py)

#### -add an integer to an array-form of integer
 - For a non-negative integer `X`, the array-form of `X `is an array of its digits in left to right order.  For example, if `X` = 1231, then the array form is [1,2,3,1].
 - Given the array-form `A` of a non-negative integer `X`, return the array-form of the integer `X+K`.
 - Note: 
  - 1 <= A.length <= 10000
  - 0 <= A[i] <= 9
  - 0 <= K <= 10000
  - If A.length > 1, then A[0] != 0
 - **Example:**
    ```python
    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000
    ```
 - [addToArray-formOfInt](https://github.com/tristaaa/lcproblems/blob/master/add2arrayformofint.py)

#### -add two binary strings
 - Given two binary strings, return their sum (also a binary string).
 - The input strings are both non-empty and contains only characters 1 or 0.
 - **Example:**
    ```python
    Input: a = "11", b = "1"
    Output: "100"

    Input: a = "1010", b = "1011"
    Output: "10101"
    ```
 - [addBinary](https://github.com/tristaaa/lcproblems/blob/master/addbinary.py)

#### -add two integer strings
 - Given two non-negative integers `num1` and `num2` represented as string, return the sum of `num1` and `num2`.
 - Note: 
  - The length of both num1 and num2 is < 5100.
  - Both num1 and num2 contains only digits 0-9.
  - Both num1 and num2 does not contain any leading zero.
  - You must not use any built-in BigInteger library or convert the inputs to integer directly.
 - [addStrings](https://github.com/tristaaa/lcproblems/blob/master/addstrings.py)

#### -add two numbers using bit manipulation
 - Calculate the sum of two integers a and b, but you are not allowed to use the operator `+` and `-`.
 - **Example:**
    ```python
    Input: a = -2, b = 3
    Output: 1
    ```
 - [addTwoNumBitOps](https://github.com/tristaaa/lcproblems/blob/master/addtwonumBitOps.py)
  - Extension: [A summary: how to use bit manipulation to solve problems easily and efficiently](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)

#### - ***multiply integer strings***
 - Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
 - **Example:**
    ```python
    Input: num1 = "123", num2 = "456"
    Output: "56088"
    ```
 - [multiplyNumbers](https://github.com/tristaaa/lcproblems/blob/master/multiplynum.py)


### 3.2 Add Digits
 - Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
 - Given a solution with O(1) running time.
 - **Example:**
    ```python
    Input: 38
    Output: 2 
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
        Since 2 has only one digit, return it.
    ```
 - [addDigits](https://github.com/tristaaa/lcproblems/blob/master/adddigits.py)



## | Substring problems
### 4.1 Repeated Substring
 - Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
 - You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
 - **Example:**
    ```python
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

    Input: "aba"
    Output: False
    ```
 - [repeatedSubstr](https://github.com/tristaaa/lcproblems/blob/master/isrepeatedsubstr.py) 


### 4.2 Longest Substring
#### -longest substring w/o repeating chars
 - Given a string, find the length of the longest substring without repeating characters.
 - **Example:**
    ```python
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    ```
 - [longestSubstrWORepeatingChars](https://github.com/tristaaa/lcproblems/blob/master/lssworeapeatingchars.py)

#### -longest palindromic substring 
 - Given a string s, find the longest palindromic substring in s. 
 - You may assume that the maximum length of s is 1000.
 - **Example:**
    ```python
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Input: "cbbd"
    Output: "bb"
    ```
 - [longestPalindromicSubstr](https://github.com/tristaaa/lcproblems/blob/master/lsspalindromic.py)


### 4.3 Count Binary Substrings
 - Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
 - Substrings that occur multiple times are counted the number of times they occur.
 - **Example:**
    ```python
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

    Notice that some of these substrings repeat and are counted the number of times they occur.

    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
    ```
 - [cntBinarySubstr](https://github.com/tristaaa/lcproblems/blob/master/cntbinarysubstr.py)



## | Palindrome problems
### 5.1 Valid Palindrome 
#### -basic 
 - Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 - Note: For the purpose of this problem, we define empty string as valid palindrome.
 - **Example:**
    ```python
    Input: "A man, a plan, a canal: Panama"
    Output: true
    ```
 - [validPalindrome](https://github.com/tristaaa/lcproblems/blob/master/palindromevalid.py)

#### -can delete one char
 - Given a non-empty string s, you may delete at most one character. 
 - Judge whether you can make it a palindrome.
 - Note: 
  - The string will only contain lowercase characters a-z. 
  - The maximum length of the string is 50000.
 - **Example:**
    ```python
    Input: "aba"
    Output: True

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.
    ```
 - [validPalindromeII](https://github.com/tristaaa/lcproblems/blob/master/palindromevalidii.py)


### 5.2 Palindrome Number



### 5.3 Palindrome Linked List
 - Given a singly linked list, determine if it is a palindrome.
 - **Example:**
    ```python
    Input: 1->2->2->1
    Output: True
    ```
 - [palindromell](https://github.com/tristaaa/lcproblems/blob/master/palindromell.py)



