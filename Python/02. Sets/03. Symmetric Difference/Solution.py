# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Difficulty: Easy
# Score: 10

a = int(input())
set_a = set(map(int,input().split()))
b = int(input())
set_b = set(map(int,input().split()))
# * unpacks the list. it means that it treats each element of the list separately
print(*sorted(set_a.symmetric_difference(set_b)),sep="\n")

