# import nest_asyncio
from fastapi import FastAPI

from config.utils import create_db_tables
from routes.index import user_router

app = FastAPI(title = "FASTAPI")

app.include_router(user_router)

attendance_data = None

create_db_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
