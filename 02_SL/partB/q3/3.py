class senrev:
    sentence = ''
    vowel = 0
    vowels = ['a','e','i','o','u']
    reverse = ''

    def __init__(self , sentence):
        self.sentence = sentence
        self.revsentence()
    def revsentence(self):
        self.reverse = ' '.join(reversed(self.sentence.split()))
    def vowelsum(self):
        self.vowel = sum(s in self.vowels for s in self.sentence.lower())
        return self.vowel
    def getrevsentence(self):
        return self.reverse


items = []

for i in range(3):
    ip = input('enter a phrase: ')
    revip = senrev(ip.strip())
    items.append(revip)
    print()


sorteditems = sorted(items, key=lambda item: item.vowelsum(), reverse=True)


for i in range(len(sorteditems)):
    x = sorteditems[i].vowelsum()
    print(f'reverse {sorteditems[i].getrevsentence()} and vowelcount {x}')
