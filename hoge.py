import collections
c = "ctact".count('c')
a = "ctact".count('a')
t = "ctact".count('t')

def test1(s):
    dic =collections.Counter(s)
    result = []
    if len(dic) != 2:
        result.append(0)
    else:
        result.append(max(dic.values()))
for C in 'cat':
    result.append(max -dic[0])
result.append(min(dic.values() - dic['c']))
result.append(min(dic.values() - dic['a']))
result.append(min(dic.values() - dic['t']))
    return result

def displey(l):
    print('/n'.join(l))

if __name__ == '__name__':
    s = input()
    result = test1(s)
    displey(result)
