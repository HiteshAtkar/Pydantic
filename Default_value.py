from pydantic import BaseModel

class car(BaseModel):
    brand:str="BMW"
    model:str

car=car(model='M4-Compitition')

print(car)