import random


class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = random.choice(["Šiaurė", "Rytai", "Pietūs", "Vakarai"])
        self.target = Target
        self.suviai = {"Šiaurė": 0, "Rytai": 0, "Pietūs": 0, "Vakarai": 0}
        self.points = 100

    def pirmyn(self):
        if self.kryptis == "Šiaurė":
            self.y += 1
        elif self.kryptis == "Rytai":
            self.x += 1
        elif self.kryptis == "Pietūs":
            self.y -= 1
        elif self.kryptis == "Vakarai":
            self.x -= 1
        self.points -= 10

    def atgal(self):
        if self.kryptis == "Šiaurė":
            self.y -= 1
        elif self.kryptis == "Rytai":
            self.x -= 1
        elif self.kryptis == "Pietūs":
            self.y += 1
        elif self.kryptis == "Vakarai":
            self.x += 1
        self.points -= 10

    def kairen(self):
        if self.kryptis == "Šiaurė":
            self.kryptis = "Vakarai"
        elif self.kryptis == "Rytai":
            self.kryptis = "Šiaurė"
        elif self.kryptis == "Pietūs":
            self.kryptis = "Rytai"
        elif self.kryptis == "Vakarai":
            self.kryptis = "Pietūs"

    def desinen(self):
        if self.kryptis == "Šiaurė":
            self.kryptis = "Rytai"
        elif self.kryptis == "Rytai":
            self.kryptis = "Pietūs"
        elif self.kryptis == "Pietūs":
            self.kryptis = "Vakarai"
        elif self.kryptis == "Vakarai":
            self.kryptis = "Šiaurė"

    def suvis(self, target):
        print("Šaunu!")
        self.target = target
        if self.target is not None:
            self.suviai[self.kryptis] += 1
            if self.x == self.target.x and self.y == self.target.y:
                print("Pataikei!")
                self.points += 50
                self.target = Target()
            else:
                self.points -= 10
                print("Praleidai taikinį.")

    def info(self):
        print("Tanko informacija:")
        print(f"Kryptis: {self.kryptis}")
        print(f"Koordinatės: ({self.x}, {self.y})")
        print(f"Šūviai: {sum(self.suviai.values())}")
        for kryptis, suviai in self.suviai.items():
            print(f"Šūviai į {kryptis}: {suviai}")
        print(f"Taškai: {self.points}")


class Target:
    def __init__(self):
        self.x = random.randint(-8, 8)
        self.y = random.randint(-8, 8)


class Game:
    def __init__(self):
        self.tank = Tankas()
        self.target = Target()
        self.points = 100
        self.top_scores = []

    def play(self):
        while self.points > 0:
            self.tank.info()
            action = input("Pasirinkite veiksmą: ")
            if action == "1":
                self.tank.pirmyn()
            elif action == "2":
                self.tank.atgal()
            elif action == "3":
                self.tank.kairen()
            elif action == "4":
                self.tank.desinen()
            elif action == "5":
                self.tank.suvis(self.target)
            elif action == "6":
                self.tank.info()
            elif action == "top":
                self.show_top_scores()
            elif action == "quit":
                break
            else:
                print("Neteisingas pasirinkimas. Bandykite dar kartą.")
            print()
        print("Žaidimas baigtas.")

    def show_top_scores(self):
        if not self.top_scores:
            print("Top rezultatų sąrašas tuščias.")
        else:
            print("Top rezultatai:")
            for i, score in enumerate(self.top_scores, start=1):
                print(f"{i}. {score['name']}: {score['score']}")

    def update_top_scores(self):
        name = input("Įveskite savo vardą: ")
        score = sum(self.tank.suviai.values())
        self.top_scores.append({"name": name, "score": score})
        self.top_scores.sort(key=lambda x: x["score"], reverse=True)
        self.top_scores = self.top_scores[:5]

    def save_top_scores(self):
        pass


game = Game()
game.play()
game.update_top_scores()
game.save_top_scores()
