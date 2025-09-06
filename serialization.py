from pydantic import BaseModel,Field,EmailStr,AnyUrl
from typing import Optional,Dict,List

class User(BaseModel):
    name: str=Field(...,max_length=20,description="Name of User")
    age: int=Field(...,description="Enter age of user")
    gender:Optional[str]=None
    Email:EmailStr=Field(description="Enter Your Personal Mail Address")
    Linkedin:AnyUrl=Field(description="Enter Your Linkedin Profile Link")
    Marks:Dict[str,int]=Field(description="Enter Subject:marks ")
    skills:List[str]=Field(description="Enter Your Skills Here")


u = User(name="Hitesh", age=23,Email="atkarhitesh@gmail.com",Linkedin="https://www.linkedin.com/in/hitesh-atkar-6734a3255/",Marks={'Python':99,'Java':80,'Math':90},skills=['Python','ML','DL','GenAI','MLOps'])

print("Model Dumped as Python Dict:",u.model_dump())
print("Model Dumped as JSON Format",u.model_dump_json())
