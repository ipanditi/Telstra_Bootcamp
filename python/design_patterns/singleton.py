class Singleton:
    _instance = None #Static
    
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
    def do_something(self):
        print("Doing Something...")

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)

singleton1.do_something()
singleton2.do_something()