class Solution:
    def fib(self, n: int) -> int:
        f0 , f1 = 0,1
        if n == 0:
            return f0
        if n == 1:
            return f1
        else:
            for i in range(n - 1):
                temp = f0 + f1
                f0 = f1
                f1 = temp
        
        return f1