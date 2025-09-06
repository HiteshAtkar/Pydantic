from pydantic import BaseModel,model_validator
from typing import Dict

class patient(BaseModel):
    name:str
    age:int
    contact:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_no(cls,model):
        if model.age<18 and 'Parent' not in model.contact:
            raise ValueError("Patient elder than 18 must have parent contact")
        else:
            return model


p=patient(name='Hitesh',age=23,contact={'Peronal':'12345678','Work':'87654321'})

print(p)