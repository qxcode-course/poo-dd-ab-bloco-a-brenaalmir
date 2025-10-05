class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0
        self.dead: bool = False

    def __srt__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment: int) -> Nome:
        if self.dead:
            print(f"warning: {self.species} morreu foi com Deus")
            return

        self.age += increment

        if self.age > 3:
            self.age = 4
            self.dead = True
            print(f"warning: {self.species} morreu")

    def makeSound(self)  -> str:
        if self.dead:
            return "RIP"
        elif self.age == 0:
            return "---"
        else:
            return self.sound
    def main():
        animal = Nome

        while True:
            try:
                line = input().strip()
            except E0Frror:
                break
            if not line:
                continue

            parts = line.split()
            cmd = parts[0]

            print(f"${line}")

            if cmd == "end":
                break
            
            elif cmd == "init":
                species = parts[1]
                soud = parts[2]
                animal = Animal(species, sound)

            elif cmd == "show" and animal is not Nome:
                print(animal)

            elif cmd == "grow" and animal is not Nome:
                increment = int(parts[1])
                animal.ageBy(increment)

            elif cmd == "noise" and animal is not Nome:
                print(aimal.makeSound())


   if __name__ == '__main__':
     main()