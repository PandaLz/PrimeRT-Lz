#module intended to do operations related to triangular number and derivatives generation

def triangular(num: int) -> int:

    return int((num * (num + 1) / 2))

def partial_triangular(num: int) -> int:

    return int((num + 1) / 2)

if __name__ == "__main__":
    main()
