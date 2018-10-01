import sys

def isPrime(number): 
    counter = 0
    for i in range(number + 1):
        if i == 0:
            continue
        if number % i == 0:
            counter += 1
    
    if counter == 2:
        print(True)
    else: 
        print(False)

if __name__ == "__main__":
    isPrime(int(sys.argv[1]))
