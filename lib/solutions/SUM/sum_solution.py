
class SumSolution:
    
    def compute(self, x: int, y: int):
        if type(x) is not int or type(y) is not int:
            raise TypeError("Incorrect type")
        
        return x + y

