from fastapi import Body, Path, Query, APIRouter
from data.data_initial import movies


router = APIRouter (
    prefix='/movie',
    tags=["movies"]
)

@router.get('/')
def hello_world():
    # Permite retornar cualquier cosa
    return "Hello world from movie"

@router.get("/movies")
def get_movies():
 return movies;

@router.get("/movies_by_id/{id}")
def get_movies_by_id(id:int = Path(ge=1, le=2000)):
    for item in movies:
        if item["id"]==id:
            return item
    return []
    
@router.get("/movies_by_categories/")
def movies_by_categories(category: str = Query(min_length=5, max_length=15)):
    return [item for item in movies if item["category"]==category]

@router.post("/new_movie")
def new_movie(id: int = Body(),title: str = Body(), overview: str = Body(), years: int = Body(), rating: int = Body(), category: str = Body()):
    movies.append({
        "id":id,
        "title":title,
        "overview":overview,
        "years":years,
        "rating":rating,
        "category":category
    })
    return movies

@router.put('/movies/{id}')
def update_movie(id:int,title:str = Body(),overview:str = Body(),year:int = Body(),rating:float = Body(),category:str = Body()):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["year"] = year
            movie["rating"] = rating
            movie["category"] = category
            return movies
        return[] 

@router.delete('/movies/{id}')
async def delete_movie(id: int) -> dict:
    for index, item in enumerate(movies):
        if item["id"] == id:
            del movies[index]
            movies.remove(item)
            return movies
    
    