def check(l: list):
    # we're going to be using the checkWithSet method since it should be more efficient!
    seen = set()
    for num in l:
        if num in seen:
            return True
        seen.add(num)
    return False


print(check([1, 2, 3, 2]))          # should print True
print(check([5, 2, -10, 44, 90]))   # should print False