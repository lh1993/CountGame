#!/usr/bin/python

from operator import sub, add, floordiv, mul
from random import randint, choice

ops = {'+': add, '-': sub, '*': mul, '/': floordiv}
MAX_TRIES = 2

def do_count():
    op = choice('+-*/')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    # print nums
    # print sub(*nums)
    # print op
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    opers = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print("you are right")
                break
            if opers == MAX_TRIES:
                print "sorry...the answer\n%s %d" % (pr, ans)
            else:
                print "you are wrong....try it again"
                opers += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print "invalid input....try again"

def main():
    while True:
        do_count()
        try:
            opt = raw_input("Again? [y | n] ").lower()
            if opt[0] == "n":
                break
        except (KeyboardInterrupt, EOFError, ValueError, IndexError):
            break

if __name__ == '__main__':
    main()
