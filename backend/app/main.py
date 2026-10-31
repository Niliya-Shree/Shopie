from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models  # noqa: F401  (registers tables)
from app.core.config import settings
from app.core.database import Base, SessionLocal, engine
from app.routers import health, products
from app.seed import seed_products


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.APP_ENV == "development":
        Base.metadata.create_all(bind=engine)
        with SessionLocal() as db:
            seed_products(db)
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="Shopie API", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router, prefix="/api")
    app.include_router(products.router, prefix="/api")
    return app


app = create_app()