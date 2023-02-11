class Profile():
    def __init__(self, name='名無し', age=' '):
        self.name = name
        self.age = age

    def introduce(self):
        return f'私の名前は{self.name}です。年齢は{self.age}歳です。'

class ExtendedProfile(Profile):
    def __init__(self, name='名無し', age=' '):
        super().__init__(name, age)
    def ask_question(self):
        return f'あなたの自己紹介をお願いします。'

instance1 = Profile()
instance1.introduce()

instance2 = ExtendedProfile()
instance2.ask_question()
instance2.introduce()
