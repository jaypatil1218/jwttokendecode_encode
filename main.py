from fastapi import Depends, FastAPI

from app.configs.Environment import get_environment_variables
from app.metadata.Tags import Tags
from app.models.BaseModel import init
from app.api.v1.access_endpoints.UserRouter import UserRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

# Add Routers

app.include_router(UserRouter)


init()
