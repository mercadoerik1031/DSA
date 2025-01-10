"""
https://leetcode.com/problems/happy-number/description/

In number theory, a happy number is defined as a number that, when repeatedly subjected
to the process of squaring its digits and summing those squares, eventually
leads to 1.

An unhappy number will never reach 1 during this process, and will
get stuck in an infinite loop.

Given an integer, determine if its a happy number.

Example:
    Input: n = 23
    Output: True
    Explanation: 2^3 + 3^2 = 13 --> 1^2 + 3^2 = 10 --> 1^2 + 0^2 = 1
"""


def is_happy_number(n: int) -> bool:
    if n < 0:
        raise ValueError

    slow = fast = n

    while True:
        slow = get_sum(slow)
        fast = get_sum(get_sum(fast))

        if fast == 1:
            return True

        elif fast == slow:
            return False


def get_sum(num: int) -> int:
    summ = 0

    while num > 0:
        summ += (num % 10) ** 2
        num //= 10

    return summ


# Time Complexity: O(log n), Space Complexity: O(1)
