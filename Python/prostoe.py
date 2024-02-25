def prost(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(17)
    print("Число простое?", prost(n))

if __name__ == '__main__':
   main()

