from pydantic import BaseModel, Field
from typing import Annotated

class product(BaseModel):
    name:Annotated[str,Field(max_length=6,description="Enter your product name")]
    prise:Annotated[float,Field(gt=10000,lt=20000,description="Enter prise bet 10k to 20k")]

p=product(name='Iphone',prise=15999.90)

print(p)