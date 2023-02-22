def rotate_array(l, k):
    for _ in range(k):
        l = shift(l)
    return l

def shift(l):
    result = []
    for i in range(len(l)):
        if i == len(l)-1:
            result.insert(0, l[i])
        else:
            result.append(l[i])
    return result


if __name__ == '__main__':
    a1 = [1, 2, 3, 4] 
    k1 = 1
    print("Input: [1, 2, 3, 4], 1")
    print("Expecting: [4, 1, 2, 3]")
    print(rotate_array(a1, k1))

    print("""
Input: [1, 2, 3], 2
Output: [2, 3, 1]
""")
    print(rotate_array([1, 2, 3], 2))
