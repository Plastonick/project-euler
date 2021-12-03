
class Card:
    suit = None
    rank = None

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank


class Hand:
    cards = None

    def __init__(self, cards) -> None:
        cards.sort(key=lambda x: x.rank, reverse=True)

        self.cards = cards

    def print(self) -> None:
        out = ""

        for card in self.cards:
            out += str(card.rank)
            out += card.suit
            out += " "

        out += " -- "
        out += str(self.getRankScore())

        print(out)

    def beats(self, hand) -> bool:
        return self.getScore() > hand.getScore()

    def getScore(self) -> int:
        mainScore = self.getMainScore() * pow(17, 5)
        rankScore = self.getRankScore()

        return mainScore + rankScore

    def getMainScore(self) -> int:
        isStraight = self.isStraight()
        isFlush = self.isFlush()

        if isStraight and isFlush:
            return 10

        if self.hasXOfAKind(x=4):
            return 9

        if self.isFullHouse():
            return 8

        if isFlush:
            return 7

        if isStraight:
            return 6

        if self.hasXOfAKind(x=3):
            return 5

        if self.isTwoPair():
            return 4

        if self.hasXOfAKind(x=2):
            return 3

        return 2

    def isFlush(self) -> bool:
        counts = {"C": 0, "S": 0, "H": 0, "D": 0}

        for card in self.cards:
            counts[card.suit] += 1

        return 5 in counts.values()

    def isStraight(self) -> bool:
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)

# project euler doesn't seem to consider ace being low
        # if self.ranksInOrder(ranks=ranks):
        #     return True

        # # consider ace low
        # if ranks[0] == 14:

        #     ranks[0] = 1
        #     ranks.sort(reverse=True)

        return self.ranksInOrder(ranks=ranks)

    def isFullHouse(self) -> bool:
        counts = self.getFrequencyCounts()
        frequencies = counts.values()

        return 2 in frequencies and 3 in frequencies

    def isTwoPair(self) -> bool:
        counts = self.getFrequencyCounts()
        frequencies = counts.values()

        numPairs = 0
        for freq in frequencies:
            if freq == 2:
                numPairs += 1

        return numPairs == 2

    def ranksInOrder(self, ranks) -> bool:
        curr = ranks[0]
        for rank in ranks[1:5]:
            if rank + 1 != curr:
                return False
            else:
                curr = rank
        return True

    def hasXOfAKind(self, x) -> bool:
        counts = self.getFrequencyCounts()

        return x in counts.values()

    def getFrequencyCounts(self) -> dict:
        counts = {}

        for card in self.cards:
            rank = card.rank

            if rank not in counts:
                counts[rank] = 0

            counts[rank] += 1

        return counts

    def getRankScore(self) -> int:
        frequencies = self.getFrequencyCounts()
        ranksFreqs = []
        for card in self.cards:
            ranksFreqs.append((card.rank, frequencies[card.rank]))

        sortedRanks = sorted(
            ranksFreqs, key=lambda x: (x[1], x[0]), reverse=True)

        score = 0
        for i in range(0, 5):
            rank = sortedRanks[i][0]

            score += rank * pow(15, 4 - i)

        return score


def cardFromString(string) -> Card:
    rankChar = string[0]

    if rankChar.isnumeric():
        rank = int(rankChar)
    else:
        rankVal = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        rank = rankVal[rankChar]

    return Card(suit=string[1], rank=rank)


poker = open("poker.txt", "r")

p1Wins = 0
p2Wins = 0
for line in poker:
    cardStrings = line.split()
    cards = list(map(cardFromString, cardStrings))

    hand1 = Hand(cards=cards[0:5])
    hand2 = Hand(cards=cards[5:10])

    # p1Score = hand1.getScore()
    # p2Score = hand2.getScore()

    # if p1Score > p2Score:
    #     p1Wins += 1
    # else:
    #     p2Wins += 1

    # if hand1.getMainScore() > 2 and hand1.getMainScore() == hand2.getMainScore():
    #     hand1.print()
    #     hand2.print()
    #     print(hand1.beats(hand2))
    #     print()

    if hand1.beats(hand2):
        p1Wins += 1
    else:
        p2Wins += 1


poker.close()

print(p1Wins)
print(p2Wins)
