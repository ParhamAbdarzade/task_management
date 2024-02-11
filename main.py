from fastapi_app import fastapi_app
from api import router

fastapi_app.include_router(router)


