import logging
import uvicorn
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import update_time
from utils import connect, delte_id

app = FastAPI()
# 允许所有的跨域请求，安全性交给防火墙负责
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 添加其他文件的路由
app.include_router(update_time.router)


@app.get("/db/{database}/{collection}", response_model=list[dict[str, Any]])
async def get_collection_data(database: str, collection: str):
    database_obj = connect[database]
    if collection not in database_obj.list_collection_names():
        logging.error("数据库中没有对应的表")
        return []
    coll = database_obj[collection].find({}).to_list()
    return await delte_id(coll)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
