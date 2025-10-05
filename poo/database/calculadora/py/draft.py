class Calculadora:
    def __init__(self, batteryMax: int):
        self.display: float = 0.0
        self.battery: int = 0  
        self.batteryMax: int = batteryMax

    def charge(self, increment: int) -> None:
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: float, b: float) -> str:
        if self.battery <= 0:
            return "fail: bateria insuficiente"
        self.battery -= 1
        self.display = a + b
        return "ok"

    def div(self, num: float, den: float) -> str:
        if self.battery <= 0:
            return "fail: bateria insuficiente"
        if den == 0:
            return "fail: divisao por zero"
        self.battery -= 1  
        self.display = num / den
        return "ok"

    def get_display(self) -> float:
        return self.display

    def get_battery(self) -> int:
        return self.battery


def main():
    calc: Calculadora | None = None

    while True:
        cmd = input()
        parts = cmd.split()
        if not parts:
            continue

        if parts[0] == "init":
            batteryMax = int(parts[1])
            calc = Calculadora(batteryMax)
            print(f"$init {batteryMax}")

        elif parts[0] == "show":
            if calc is None:
                continue
            print("$show")
            display = calc.get_display()
            battery = calc.get_battery()
            print(f"display = {display:.2f}, battery = {battery}")

        elif parts[0] == "charge":
            if calc is None:
                continue
            inc = int(parts[1])
            calc.charge(inc)
            print(f"$charge {inc}")

        elif parts[0] == "sum":
            if calc is None:
                continue
            a = float(parts[1])
            b = float(parts[2])
            result = calc.sum(a, b)
            print(f"$sum {int(a) if a.is_integer() else a:g} {int(b) if b.is_integer() else b:g}")
            if result != "ok":
                print(result)

        elif parts[0] == "div":
            if calc is None:
                continue
            num = float(parts[1])
            den = float(parts[2])
            result = calc.div(num, den)
            print(f"$div {int(num) if num.is_integer() else num:g} {int(den) if den.is_integer() else den:g}")
            if result != "ok":
                print(result)

        elif parts[0] == "end":
            print("$end")
            break

        else:
            print(f"$unknown command: {cmd}")


if __name__ == "__main__":
    main()