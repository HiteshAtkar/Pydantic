from pydantic import BaseModel,computed_field

class rectangle(BaseModel):
    length:int
    breadth:int

    @computed_field
    @property
    def area(self)->float:
        area=round((self.length*self.breadth),2)
        return area

r=rectangle(length=20,breadth=10)

print(r)
print(r.area)