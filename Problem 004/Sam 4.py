__author__ = 'samschickler'

def main():
    greatest = 0
    for a in range(100, 999):
        for b in range(100, 999):
            prod = a * b
            if prod > greatest and (str(prod)[::-1]) == str(prod):
                greatest = prod
    print(greatest)

if __name__ == "__main__":
    main()
