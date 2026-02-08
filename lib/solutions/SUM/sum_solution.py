
class SumSolution:
    
    def compute(self, x: int, y: int):
        if not all(isinstance(i, int) for i in (x, y)):
            raise ValueError("Both x and y must be integers")
        
        return x + y
