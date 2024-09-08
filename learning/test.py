arr = [3, 5, 34, 6, -2, 11, 49, 6, 84, 0, 1]

preSum = [0] * (len(arr) + 1)

for i in range(1, len(arr) + 1):
    preSum[i] = preSum[i - 1] + arr[i - 1]


def sumRange(arr, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += arr[i]  

sumRange(arr, 3, 7)