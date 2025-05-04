import logging
import uvicorn
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

connect = MongoClient(host="localhost", port=27017)

app = FastAPI()
# 允许所有的跨域请求，安全性交给防火墙负责
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] ,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def delte_id(documents: list) -> list:
    docs_without_id = []
    for doc in documents:
        doc_without_id = {key: value for key, value in doc.items() if key != '_id'}
        docs_without_id.append(doc_without_id)
    print(docs_without_id)
    return docs_without_id

@app.get("/db/{database}/{collection}", response_model=list[dict[str, Any]])
async def get_collection_data(database: str, collection: str):
    database_obj = connect[database]
    if collection not in database_obj.list_collection_names():
        logging.error("数据库中没有对应的表")
        return []
    coll = database_obj[collection].find({}).to_list()
    return await delte_id(coll)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=7999, log_level="info")