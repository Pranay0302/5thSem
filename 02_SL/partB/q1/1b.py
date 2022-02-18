from collections import Counter

def word_count(file):
    with open(file) as e:
        x = e.read().split()
        c = Counter(x)
        print(c)

word_count('1bt.txt')
