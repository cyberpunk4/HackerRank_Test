# Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Difficulty: Easy
# Score: 10
def average(array):
    unique_elements = set(array)
    return ((sum(unique_elements)) / len(unique_elements))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)