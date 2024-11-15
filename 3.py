class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        total = 0
        for n in range(1, N + 1):
            total += self.transform(n)
        return total


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)

power_summator = PowerSummator(3)  
result_power = power_summator.sum(3)  
print(f"Сумма кубов от 1 до 3: {result_power}") 

square_summator = SquareSummator()  
result_square = square_summator.sum(3) 
print(f"Сумма квадратов от 1 до 3: {result_square}") 

cube_summator = CubeSummator() 
result_cube = cube_summator.sum(3) 
print(f"Сумма кубов от 1 до 3: {result_cube}") 
