from pydantic import BaseModel

class Address(BaseModel):
    house_no:int
    city:str
    pin:int

class student(BaseModel):
    name:str
    roll:int
    adress:Address

a=Address(house_no=1,city="Pune",pin=412409)
s=student(name="Hitesh",roll=48,adress=a)

print(s)
