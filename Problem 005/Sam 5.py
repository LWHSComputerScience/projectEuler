__author__ = 'samschickler'

def main():
    val = 1
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 2, 2, 2, 3]
    for s in nums:
        val *= s
    print(val)


if __name__ == "__main__":
    main()
