# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Difficulty: Medium
# Score: 50
# first method we can also use underscore(_) instead of a and b
a, b = map(int,input().split())
lst = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum([(i in like) - (i in dislike) for i in lst]))

# second method without using sum function
'''_ = map(int,input().split())
lst = input().split()
like = set(input().split())
dislike = set(input().split())
happiness = 0
for i in lst:
    if i in like:
        happiness += 1
    if i in dislike:
        happiness -= 1
print(happiness)'''

