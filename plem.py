class Village:
    def __init__(self, coords, pike, swords, heavycav):
        self.coords = coords
        self.pike = pike
        self.swords = swords
        self.heavycav = heavycav

    def countPikesSwords(self):
        if self.pike != "?" or self.swords != "?":
            return int(self.pike) + int(self.swords)
        else:
            return '?'

    def __str__(self):
        return self.coords + ": Pikemans: " + self.pike + ", Swordsmans: " + self.swords + ", Heavy Cavalary: " + self.heavycav


file = open("villages.txt", 'r').read().split('\n')
villagesTab = []

for line in file:
    possibleVillage = string.split(",")
    if possibleVillage[1] == "w wiosce":
        try:
            villagesTab.append(Village(possibleVillage[0], possibleVillage[2], possibleVillage[3], possibleVillage[7]))
        except:
            print("Check the file format")

for village in villagesTab:
    supportNumb = village.countPikesSwords()
    try:
        supportNumb //= 200
    except:
        supportNumb = '?'
    print("\nVillage: " + str(village) + "\n" + "Support packages to send: " + str(supportNumb))
