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
            print("fail: Não há ninguem no carro")
        
    def fuel(self, amount: int) -> None:
        if amount< 0:
            return
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int) -> None:
        if self.passengers == 0:
            print("fail: Não há ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= distance:
            self.km += distance
            self.gas -= distance
        else:
            print(f"fail: tanque vazio após andar {self.gas} km")
            self.km += self.gas
            self.gas = 0

def main() -> None:
    carro = Carro()
    while True:
        