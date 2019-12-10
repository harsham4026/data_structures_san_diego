#python3


#define function

def fibonacci(x):
    if (x<2):
        return x
    else:
        a = list(range(x+1))
        a[0] = 0
        a[1] = 1
        for i in range(2,x+1):
            a[i] = a[i-1] + a[i-2]
        return a[x-1] % 10



if __name__ == '__main__':
    y = int(input())
    print(fibonacci(y))
