n = input()
def count(word, s):
    n = 0
    for i in range(len(s) -2):
        if s[i: i + 3] == "word
        n += 1

    return n

def count2(word, s):
    return s.count(word)

def display(n):
    print(n)


if __name__ == '__main__':
    s = input()
    result = count2('cat', s)
    display(result)
