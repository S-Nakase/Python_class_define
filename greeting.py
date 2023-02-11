class Greeting():
    def __init__(self, name='名無し'):
        self.name = name

    def morning(self):
        print(f'{self.name}、おはようございます！')

    def evening(self):
        print(f'{self.name}、こんばんは！')

# name1 = Greeting()
# name1.morning()
# name1.evening()
