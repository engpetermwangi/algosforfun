# Problem
[**Challenge Nine**](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997#problem) from Round A 2022 of [Google Kick Start](https://codingcompetitions.withgoogle.com/kickstart)

# Solutions in Python3
## [Naive](./challenge_nine_naive.py)
1. Brute-force through all the possible digits `0..9` that can be inserted
2. Test for divisibility of all possible new numbers with the digit inserted in all possible locations in the number
3. Find the minimum of all the new number numbers that are divisible by 9

## [Efficient](./challenge_nine_efficient.py)
1.  Make use of the divisibity test of 9 to find out which digit to add in *O(L)* time where *L* is the number of digits in the number
    * if the number is already divisible by 9, insert a 0(or 9 but clearly 0 will result into the smallest possible number)
    * a  number is divisible by 9 iff the sum of its digits is divisible by 9
2.  insert the digit *d* as far right as possible, right before a digit *k* such that *d < k* in *O(L)* time
    * careful not to insert 0 as a leading zero
