from pydantic import BaseModel, AnyUrl

class url(BaseModel):
    url:AnyUrl

u=url(url="https://github.com/HiteshAtkar")
print(u.url)