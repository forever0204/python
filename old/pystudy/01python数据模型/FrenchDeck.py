import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 创建纸牌类
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 定义纸牌的数字
    suits = 'spades diamonds clubs hearts'.split()
    # 定义纸牌的花色 黑桃 梅花 方片 红心
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    # 初始化纸牌
    def __len__(self):
        return len(self._cards)
    # 纸牌的长度
    def __getitem__(self, position):
        return self._cards[position]
#     根据纸牌的位置得到纸牌
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
#将牌进行排序

beer_card = Card('1', 'diamonds')
print(beer_card)
# 输出自定义的牌
deck = FrenchDeck()
print(deck.ranks)
print(deck.suits)
# 输出deck内的所有花色和数字
print(deck[0],deck[-1])
print(choice(deck))
# 随机抽取一张牌
print(deck[:3])
# 输出最上面3张牌（切片）
print(deck[12::13])
# 输出牌面A（切片）
for card in deck:
    print(card)
    # 迭代牌面
print('--------------------------------')
for card in reversed(deck):
    print(card)
    # 反向迭代
print('--------------------------------')
for card in sorted(deck, key=spades_high):
    print(card)
#利用排序进行输出