class   calculator:
    def __init__(self, num1:int, num2:int) -> None:
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def rem(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 // self.num2
