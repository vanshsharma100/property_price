from pydantic import Field,BaseModel,computed_field,EmailStr,field_validator
from typing import Annotated,List,Optional,Literal
from config.city_tier import city_tier_1


class userinput(BaseModel):
    area_sqft:Annotated[float,Field(...,gt=0,description="enter area (sqft)")]
    location:Annotated[str,Field(...,description='enter which location user prefer')]
    property_category:Annotated[Literal["Farmhouse","Apartment","Residential"],Field(description="user enters property category")]
    property_type:Annotated[Literal['3BHK','2BHK','1BHK','Villa','Commercial'],Field(description="enter type of property user wants")]
    distance_hospital_km:Annotated[float,Field(default=5.0,gt=0,description="enter aprroximate distance from hospital")]
    distance_airport_km:Annotated[float,Field(default=5.0,gt=0,description="enter aprroximate distance from airport")]
    zone:Annotated[Literal['Urban','Semi-Urban'],Field(description="enter zone which user wants out of urban or semi-urban")]
    @field_validator('location')
    @classmethod
    def normalize_loc(cls,v:str)->str:
        v=v.strip().title()
        return v


    @computed_field
    @property
    def tier_city(self)->int:
        if self.location in city_tier_1:
            return 1
        else:
            return 2