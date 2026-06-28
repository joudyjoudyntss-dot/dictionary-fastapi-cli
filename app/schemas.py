from pydantic import BaseModel,Field
from typing import Optional
class wordbase(BaseModel):
    word:str=Field(...,min_length=2,max_length=100)
    definition:str=Field(...,min_length=3,max_length=300)
    example: Optional[str] = Field(default=None, max_length=300)
class wordcreate(wordbase):
    pass
class wordresponse(wordbase):
    id:int
    class Config:
        from_attributes = True