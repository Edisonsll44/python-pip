from fastapi import APIRouter
from api.movie_api import router as v1_movie_router
from api.schema_api import router as v1_schema_router

routers = APIRouter()

router_list = [v1_movie_router,v1_schema_router]

for router in router_list:
    router.tags = router.tags.append("v1")
    router.include_router(router)
 
