from multiprocessing import Pool
import time

def factorial(n):
    #ending condition
    if n <= 1:
        return 1

    #reducing condition
    return n * factorial(n-1)

def fib_iter(n):
    res = [0 for i in range(n)]
    res[0] = 1
    res[1] = 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[n-1]

def fibonacci(n):
    if(n<=2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main(n):
    print("\nStart for ", n, "\n")
    start_time = time.time()
    #output = factorial(n)
    #output = fibonacci(n)
    output = fib_iter(n)
    end_time = time.time()
    print("Time to compute factorial for ", n, " is ", (round(end_time-start_time, 3)), "\n")
    return output

if __name__ == "__main__":
    
    nums = [20, 25, 30, 35, 40,100, 400, 1000, 100000]
    
    p = Pool(len(nums))
    #map (name of function to be called, list of inputs)
    res  = p.map(main, nums)
    #ans = [r.get() for r in res]
    print(res)
