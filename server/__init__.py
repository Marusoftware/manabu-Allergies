from fastapi import FastAPI
from fastapi.routing import APIRoute

def custom_generate_unique_id(route: APIRoute):
    return f"{f'{route.tags[0]}-'if len(route.tags) else ''}{route.name}"

app = FastAPI(title="ManabuAllergies API", description="API of ManabuAllergies", generate_unique_id_function=custom_generate_unique_id)

from fastapi.middleware.trustedhost import TrustedHostMiddleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost"])

from fastapi.middleware.gzip import GZipMiddleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

from starlette.middleware.sessions import SessionMiddleware
import random, string
def randomstr(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
app.add_middleware(SessionMiddleware, secret_key=randomstr(15))

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routes import router
app.include_router(router)

from tortoise.contrib.fastapi import register_tortoise
from .config import Settings
from .models import db

settings=Settings()

db_config={
    "connections":{
        "default":{
            "engine":"tortoise.backends.asyncpg",
            "credentials":{
                "host":settings.postgres_host,
                "port":settings.postgres_port,
                "user":settings.postgres_user,
                "password":settings.postgres_password,
                "database":settings.postgres_db
            }
        }
    },
    "apps":{
        "models": {
            "models":[db, 'aerich.models'],
            'default_connection': 'default'
        }
    }
}
register_tortoise(app=app, config=db_config, add_exception_handlers=True)