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

    def evaluate_once(self):
        f = self.function
        if f(self.xl) * f(self.xu) >= 0 :
            raise Exception("f(xl) * f(xu) must be lower than 0");
        xr = ( self.xl + self.xu )/2
        
        if f(self.xl) * f(xr) < 0:
            return Bisection( f,self.iter_max-1, self.xl, xr)
        elif f(self.xl) * f(xr) > 0:
            return Bisection( f,self.iter_max-1, xr, self.xu )

        return 0

    def __str__(self):
        return f"[ xl={self.xl},  xu={self.xu}, iter={self.iter_max} ]"