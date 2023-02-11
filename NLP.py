import MeCab
from collections import Counter
import numpy as np
import random


class NLP():
    def __init__(self, sentence):
        self.sentence = sentence

    def pos(self):
        m = MeCab.Tagger('-Owakati')
        parsed_text = m.parse(self.sentence)
        parsed_text = parsed_text.split()
        print(parsed_text)

    def ngram_dic2(self):
        m = MeCab.Tagger('-Owakati')
        parsed_text = m.parse(self.sentence)
        txt = parsed_text.split()
        delimiter = ['「', '」', '　']
        double = list(zip(txt[:-1], txt[1:]))
        double = filter((lambda x: not((x[0] in delimiter) or (x[1] in delimiter))), double)
        dic2 = Counter(double)

        for u,v in dic2.items():
            print(u, v)

    def ngram_dic3(self):
        m = MeCab.Tagger('-Owakati')
        parsed_text = m.parse(self.sentence)
        txt = parsed_text.split()
        delimiter = ['「', '」', '　']
        triple = list(zip(txt[:-2], txt[1:-1], txt[2:]))
        triple = filter((lambda x: not((x[0] in delimiter) or (x[1] in delimiter) or (x[2] in delimiter))), triple)
        dic3 = Counter(triple)

        for u, v in dic3.items():
            print(u, v)


# sentence = NLP()
# sentence.pos()
# sentence2 = NLP()
# sentence2.ngram_dic2()
# sentence3 = NLP()
# sentence3.ngram_dic3()


# class NextWord(NLP):
#     def __init__(self, sentence):
#         super().__init__(sentence)

#     def __init__(self, words, dic):
#         self.words = words
#         self.dic = dic

#     def nextword(self):
#         grams = len(self.words)
#         if grams == 2:
#             matcheditems = np.array(list(filter(
#                 (lambda x: x[0][0] == self.words[1]),
#                 self.dic.items()
#             )))
#         else:
#             matcheditems = np.array(list(filter(
#                 (lambda x: x[0][0] == self.words[1]) and (lambda x: x[0][1] == self.words[2]),
#                 self.dic.items()
#             )))

#         if (len(matcheditems) == 0):
#             print('No matched generator for', self.words[1])
#             return ''

#         probs = [row[1] for row in matcheditems]
#         weightlist = random.rand(len(matcheditems)) * probs

#         if grams == 2:
#             u = matcheditems[np.argmax(weightlist)][0][1]

#         else:
#             u = matcheditems[np.argmax(weightlist)][0][2]

#         return u




