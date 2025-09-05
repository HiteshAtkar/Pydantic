from pydantic import BaseModel, Field
from typing import Dict

class student(BaseModel):
    name:str=Field(max_length=6,description="Enter student name here")
    roll:int=Field(gt=0,lt=100,description="Roll No should be grater than 1 and less than 100")
    marks:Dict[str,int]

s=student(name="Hitesh",roll=48,marks={'Python':99,'Java':80,'Data Structure':82})

print(s.marks)