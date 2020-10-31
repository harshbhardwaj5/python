class car:
    def __init__(self,speed):
        self.color=speed
        print("init is called",speed)

ford = car(12)
honda=car(1)
audi = car(7)
print(honda.color)
print(audi.color)
