from fastapi import APIRouter
from dto.movie import Movie
from data.data_initial import movies

router = APIRouter (
    prefix='/schema',
    tags=["schema"]
)


@router.get("/")
def get_list():
    return "Hola desde schema"



@router.post("/movies")
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@router.put("/movies/{id}")
def update_mocie(id: int, movieToUpdate: Movie):
     for movie in movies:
        if movie["id"] == id:
            movie["title"] = movieToUpdate.title
            movie["overview"] = movieToUpdate.overview
            movie["year"] = movieToUpdate.years
            movie["rating"] = movieToUpdate.rating
            movie["category"] = movieToUpdate.category
            return movies
        return[]        

    
    