from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.config_app import create_configuration_fastapi

#importacion del router
from api.movie_api import router as movie_router
from api.schema_api import router as schema_router

    
#creacion de instancia de app
app= FastAPI()
create_configuration_fastapi(app)

#inclusion de las rutas
app.include_router(movie_router)
app.include_router(schema_router)


@app.get('/', tags=["home"])
def hello_world():
        # Permite retornar cualquier cosa
        # return "Hello world"
        # return {"Hello": "World"}
        return HTMLResponse("<h2>Hello World!</h2>")

