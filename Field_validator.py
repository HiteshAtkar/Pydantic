from pydantic import BaseModel,EmailStr,field_validator

class patient(BaseModel):
    email:EmailStr

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        mail=['icici.com','axis.com']
        domain=value.split('@')[-1]
        if domain not in mail:
            raise ValueError("Not a employee from partner bank")
        else:
            return value

p=patient(email="atkarhitesh@gmail.com")

print(p)
