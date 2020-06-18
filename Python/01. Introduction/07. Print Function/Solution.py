# Problem: https://www.hackerrank.com/challenges/python-print/problem
# Difficulty: Easy
# Score: 20

if __name__ == '__main__':
    print(*range(1, int(input()) + 1), sep='')
    ''' using loop '''
    '''for i in range(1,int(input()) + 1):
        print(i,end="")'''