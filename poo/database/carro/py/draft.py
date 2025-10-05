class Carro:
    def __init__(self) -> None:
        self.passengers: int = 0
        self.passMax: int = 2
        self.km: int = 0
        self.gas: int = 0
        self.gasMax: int = 100

    def __str__(self) -> str:
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"
    
    def enter(self) -> None:
        if self.passengers < self.passMax:
            self.passengers += 1
        else:
            print("fail: limite de pessoas atingido")
        
    def leave(self) -> None:
        if self.passengers > 0:
            self.passengers -= 1
        else: 
            print("fail: nao ha ninguem no carro")
        
    def fuel(self, amount: int) -> None:
        if amount <= 0:
            return
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int) -> None:
        if self.passengers == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= distance:
            self.km += distance
            self.gas -= distance
        else:
            distancia_andada = self.gas
            self.km += distancia_andada
            self.gas = 0
            print(f"fail: tanque vazio apos andar {distancia_andada} km")

def main() -> None:
    carro = Carro()
    while True:
        line = input()
        if not line:
            continue

        print(f"${line}")
        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break
        elif cmd == "show":
            print(carro)
        elif cmd == "enter":
            carro.enter()
        elif cmd == "leave":
            carro.leave()
        elif cmd == "fuel":
            amount = int(parts[1])
            carro.fuel(amount) 
        elif cmd == "drive":
            distance = int(parts[1])
            carro.drive(distance) 

if __name__ == "__main__":
    main()