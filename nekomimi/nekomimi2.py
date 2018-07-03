import re
import collections

word = re.compile(r'cat')
alist = (word.findall(input()))
C = collections.Counter(alist)
print(C['cat'])
