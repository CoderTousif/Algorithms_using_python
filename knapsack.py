# A naive recursive implementation of 0-1 Knapsack Problem
# Returns the maximum value that can be put in a knapsack of capacity

cache = {}


def knapSack(capacity, n, weights, values):
    if n == 0 or capacity == 0:
        return 0
    elif weights[n - 1] > capacity:
        return knapSack(capacity, n - 1, weights, values)
    else:
        if n - 1 not in cache:
            # global cal
            # cal += 1
            cache[n - 1] = max(values[n - 1] + knapSack(capacity - weights[n - 1], n - 1, weights, values),
                               knapSack(capacity, n - 1, weights, values))

        return cache[n - 1]


# tabulized
def knapSackTab(W, n, wt, values):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


# Greedy approach, non optimal solution
def knapSackGreedy(capacity, n, weight, value):
    ratio = []
    for i in range(n):
        ratio.append(value[i] / weight[i])

    takenValue = 0
    ks = []

    for i in range(n):
        if capacity == 0:
            break
        maxRatio = max(ratio)
        maxIdx = ratio.index(maxRatio)

        if weight[maxIdx] <= capacity:
            # add item to the knapsack
            ks.append(value[maxIdx])
            takenValue += value[maxIdx]
            # print(value[maxIdx])
            capacity = capacity - weight[maxIdx]

        ratio.pop(maxIdx)
        value.pop(maxIdx)
        weight.pop(maxIdx)

    return ks, takenValue


# Driver program to test above function
if __name__ == '__main__':
    value = [50, 60, 100, 120, 240]
    weight = [5, 10, 20, 30, 60]
    capacity = 50
    n = len(value)
    # print(knapSack(capacity, n, weight, value))
    # print(knapSackTab(capacity, n, weight, value))
    # print(knapSackDP(capacity, n, weight, value))
    print(knapSackGreedy(capacity, n, weight, value))
    # print("number of cal", cal)
    # print(cache)

    # capacity = int(input("Enter the capacity of the knapsack: "))
    # n = int(input("Enter number of items: "))
    # values = []
    # weights = []
    # print("Enter the values of the items")
    # for i in range(n):
    #     values.append(int(input(f'Value {i+1}: ')))

    # print("Enter the weights of the items")
    # for i in range(n):
    #     weights.append(int(input(f'Weight {i + 1}: ')))

    # totalValueInKnapSack = knapSack(capacity, n, weights, values)
    # print(f'Total value in kanapsack: {totalValueInKnapSack}')
