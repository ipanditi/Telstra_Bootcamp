from abc import ABC, abstractmethod
class Interest(ABC):
    @abstractmethod
    def calculateInterest(self,principal,rate,time):
        pass
    
class SimpleInterest(Interest):
    def __init__(self,principal,rate,time):
        self.principal=principal
        self.rate=rate
        self.time=time
        
    def calculateInterest(self, principal,rate,time):
        return principal*rate*time
    
class CompoundInterest(Interest):
    def __init__(self,principal,rate,time):
        self.principal=principal
        self.rate=rate
        self.time=time
        
    def calculateInterest(self, principal, rate, time):
        Amount = principal * (pow((1 + rate / 100), time))
        CI = Amount - principal
        return CI

class CalculateInterest:
    def doCalculate(self,interest):
        p = interest.principal
        r = interest.rate
        t = interest.time
        return interest.calculateInterest(p,r,t)
        
i = CompoundInterest(100,2,3)
p = CalculateInterest()
print(p.doCalculate(i))