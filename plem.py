class Wioska:
    def __init__(self, koordy, piki, miecze, ck):
        self.koordy = koordy
        self.piki = piki
        self.miecze = miecze
        self.ck = ck

    def countPikiMiecze(self):
        if self.piki != "?" and self.miecze != "?":
            return int(self.piki) + int(self.miecze)
        else:
            return '?'

    def __str__(self):
        return self.koordy + ": Piki: " + self.piki + ", Miecze: " + self.miecze + ", CK: " + self.ck


tab = open("wioski.txt", 'r').read().split('\n')
wioskiTab = []

for string in tab:
    xy = string.split(",")
    if xy[1] == "w wiosce":
        try:
            wioskiTab.append(Wioska(xy[0], xy[2], xy[3], xy[7]))
        except:
            print("Prawdopodobnie problem z formatem pliku")

for wioska in wioskiTab:
    ilePaczek = wioska.countPikiMiecze()
    try:
        ilePaczek //= 200
    except:
        ilePaczek = '?'
    print("\nWioska: " + str(wioska) + "\n" + "Paczek do wysłania: " + str(ilePaczek))