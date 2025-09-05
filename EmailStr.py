from pydantic import BaseModel, EmailStr

class email(BaseModel):
    email:EmailStr

mail=email(email="atkarhitesh@gmail.com")
print(mail)