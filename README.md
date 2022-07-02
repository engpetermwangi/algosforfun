# Problem
[**Silly Submissions**](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5#problem) from Round H 2021 of [Google Kick Start](https://codingcompetitions.withgoogle.com/kickstart)

# Solutions in Python3
## [Naive](/silly_submissions_naive.py)
1. Use the built-in string function `str.replace` to replace the special sequence of characters with the respective character.
2. Terminate when no further changes can be done

> `str.replace` searches through the string from the start through to the end every time it's called. There is need for a more efficient way to find and update characters that need to be updated.

## [Efficient](/silly_submissions_efficient.py)
1. Create a **bidirectional linked list**, also termed as [**doubly linked list**](https://en.wikipedia.org/wiki/Doubly_linked_list) from the string while:
    * holding on to the head for the final back to string transformation
    * identifying points of interest as a mapping of each of the special sequences to a set of node instances that need the transformation like so:
        ```python
        {
            "01": set(),
            "12": set(),
            .
            .
            .
        }
        ```
    This allows each node that needs to be updated to be found and updated in contant time.
2. Transform the bidirectional linked list by going through the points of interest in the required order and making necessary changes while confirming the transformation can actually be done. This is important because certain special sequences cease to be special after transformations in neighboring sequences happen. Be sure to clear respective sets after doing the transformations.
3. Terminate when there aren't any more points of interest
4. Finally convert the bidirectional linked list to a string. Note that a recursive function to construct the string does not work for all problem sets in a Python implementation. This is due to a conservative default recursive depth of 1000. This limit is not sufficient for long output strings. You may choose to increase it to any `n` with `sys.setrecursionlimit(n)` but then `n` is platform-dependent. Use an iterative approach instead.