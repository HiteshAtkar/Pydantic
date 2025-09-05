from pydantic import BaseModel
from typing import Optional

class person(BaseModel):
    name:str
    age:int
    gender:Optional[int]=None

p=person(name='Hitesh',age=23) 
print(p)