#making memo global might be better, but works seamlessly no matter what
#fibanocci series
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
#0 1 2 3 4 5 6
#0 1 1 2 3 5 8
print('Fibonacci:', fib(103))

#grid traveler
def grid_traveller(m, n, memo={}):
    key = (m,n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n ==0: return 0

    memo[key] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)
    return memo[key]

print('GridTraveller:', grid_traveller(19, 19))

#canSum
#returns true or false
def canSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for n in numbers: #num of numbers in js
        reminder = targetSum - n
        if canSum(reminder, numbers, memo):
            memo[reminder] = True
            return True

    return False

print('canSum: ',canSum(300, [7, 3]))

#howSum
#return an array with combo of added sum (return any) or return null

def howSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for n in numbers: #num of numbers in js
        reminder = targetSum - n
        result = howSum(reminder, numbers, memo)
        if result is not None:
            memo[targetSum] = result + [n]
            return memo[targetSum]

    return None
print('canSum: ',canSum(6, [2, 1, 3]))
print('howSum: ',howSum(6, [6, 2, 3]))
#what if returned all how sums

#bestSum
#return the best possible way to find the sum, shortest
def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestComb = None

    for n in numbers:
        reminder = targetSum - n
        reminderComb = bestSum(reminder, numbers, memo)
        if reminderComb is not None:
            comb = reminderComb + [n]
            if shortestComb is None or len(comb) < len(shortestComb):
                    shortestComb = comb

    memo[targetSum] = shortestComb
    return shortestComb

print('Best Sum: ', bestSum(100, [5, 3, 4, 7]))
print(sum([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 5]))
#all sum
#return all possible way to find the sum
#could be done
#import sys
def listSums(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return [[]]
    if targetSum < 0: return None

    currentList = []

    for n in numbers:
        result = listSums(targetSum - n, numbers, memo)
        if result is not None:
            for i in result:
                currentList += [i + [n]]

    memo[targetSum] = currentList
    return currentList
#commented out to avoid high memory leak
# for i in listSums(3,[1,2,3,10]):
#     print('listSums: ', i)



