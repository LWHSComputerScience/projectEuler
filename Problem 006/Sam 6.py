__author__ = 'samschickler'

def main():
    sumsquare = 0
    squaresum = 0
    x = 1
    while x <= 100:
        sumsquare += (x ** 2)
        squaresum += x
        x += 1
    squaresum = (squaresum ** 2)
    dif = squaresum - sumsquare
    print(dif)

if __name__ == "__main__":
    main()
