from pydantic import BaseModel, Field
from typing import Optional
import datetime

# Se crea clase Movie, que hereda de BaseModel
class Movie(BaseModel):
    id: Optional[int] = None  # Otra forma
    # id: int | None = None # Una forma de definir que es opcional
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(max_length=50, min_length=15)
    """
    gt: greater than
    ge: greater than or equal
    lt: less than
    le: less than or equal
    """
    year: int = Field(le=datetime.date.today().year)
    rating: float = Field(ge=2, le=4)
    category: str = Field(min_length=3, max_length=10)

    model_config = {
        "json_schema_extra" : {
            "example":{
                "id":1,
                "title":"Mi pelicula",
                "overview":"Descripción de la película",
                "years":2023,
                "rating":9.0,
                "category":"Science Fiction"
            }
        }
    }