from fastapi import FastAPI
from routes.user import user_router
from config.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}

app.include_router(user_router, prefix='/api', tags=['user'])
