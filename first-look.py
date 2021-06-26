class Collection:

    def __init__(self):
        self.items = {}

    def add(self, key, value):
        self.items[key.lower()] = value

    def __getitem__(self, key):
        return self.items.get(key, None)

    def __setitem__(self, key, value):
        self.items[key.lower()] = value

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

items = Collection()

items['ahmad'] = 'Ahmad Manji'
items['yasin'] = 'Yasin Manji'
items['kamel'] = 'Kamel Manji'

items['barish'] = "Barish Kamali"

print(items['yasin'])
print(len(items))
print('_' * 10)
for item in items:
    print(f"{item}: {items[item]}")