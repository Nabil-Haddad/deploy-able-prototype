from pydantic import BaseModel,Field
from datetime import date


# create the post message model
class EchoRequest(BaseModel):
    text : str


# create the post insert rows model 
class Rows(BaseModel):
   date : date
   production_line : str = Field(min_length= 4, max_length= 20 ,description="The production line")
   shift : str = Field(min_length= 4, max_length= 20 ,description="The production shift")
   units_planned : int = Field(description="The number of unit planned in each line")
   units_produced : int = Field(description="The number of unit produced in each line")
   defective_units : int = Field(description="The number of units defected in each line")
   downtime_minutes : int = Field(description="The number of minutes")
