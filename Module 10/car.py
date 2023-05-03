class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    # def __str__(self):
    #     return f"{self.color},{self.mileage}"


A=Car("Blue",20000)
print(A)
print(A.color)
B=Car(color="Red",mileage=45000)

for car in (A,B):
    print(f"The {car.color} car has {car.mileage} miles")
