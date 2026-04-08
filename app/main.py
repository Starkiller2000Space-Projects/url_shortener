"""Executable file."""

from fastapi import FastAPI

from app.core import router_core
from app.database import Base, engine
from app.shorten import router_shorten
from app.stats import router_stats

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")


app.include_router(router_stats)
app.include_router(router_shorten)
app.include_router(router_core)
