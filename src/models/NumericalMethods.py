class NumericalMethods:
    def __init__( self,function,iter_max ):
        self.function = function
        self.iter_max = iter_max

    def bisection(self,xl,xu):
        return Bisection( self.function,self.iter_max,xl,xu )

class Bisection(NumericalMethods):
    def __init__( self,function,iter_max,xl,xu ):
        NumericalMethods.__init__(self,function,iter_max)
        self.xl = xl
        self.xu = xu
        self.set_xr()

    def set_xr(self):
        f = self.function
        if f(self.xl) * f(self.xu) >= 0 :
            raise Exception("f(xl) * f(xu) must be lower than 0");
        self.xr = ( self.xl + self.xu )/2
        
    def evaluate_once(self):
        f = self.function
        if f(self.xl) * f(self.xr) < 0:
            return Bisection( f,self.iter_max-1, self.xl, self.xr)
        elif f(self.xl) * f(self.xr) > 0:
            return Bisection( f,self.iter_max-1, self.xr, self.xu )

        return None

    def __evaluate(self):
        iterations = []
        current = self
        while current.iter_max > 0:
            current = current.evaluate_once()
            iterations.append(current)
        return [*iterations]
    
    def print(self,**config):
        iterations = self.__evaluate()
        for iter in iterations:
            print(iter)


    def __str__(self):
        return f"[ xl={self.xl}, xu={self.xu}, xr={self.xr}, iter={self.iter_max} ]"
