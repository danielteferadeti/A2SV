# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    maxCount = 0
    
    for a in prices:
        k -= a
        if k < 0:
            break
        else:
            maxCount += 1
    return maxCount