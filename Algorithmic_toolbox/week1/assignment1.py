#python3


#define function

def sum(x, y):
    return x + y

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(sum(x, y))
