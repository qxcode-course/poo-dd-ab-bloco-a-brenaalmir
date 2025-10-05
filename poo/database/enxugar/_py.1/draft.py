class Towel:
    def _init_(self, color: str, size: str): 
        self.color = color
        self.size = size
        self.wetness = 0

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry(self) -> bool:
        return self.wetness == 0

    def wringOut(self):
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        return 0

    def _str_(self):  
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"


def main():
    toalha = None
    while True:
        try:
            line = input()
        except EOFError:
            break

        print(f"${line}")
        args = line.strip().split()

        if not args:
            continue

        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "criar":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif cmd == "mostrar":
            if toalha is not None:
                print(toalha)
        elif cmd == "seca":
            if toalha is not None:
                print("sim" if toalha.isDry() else "nao")
        elif cmd == "enxugar":
            if toalha is not None:
                amount = int(args[1])
                toalha.dry(amount)
        elif cmd == "torcer":
            if toalha is not None:
                toalha.wringOut()
        else:
            print("fail: comando desconhecido")


if _name_ == "_main_": 
    main()