from utils.db import *


async def delte_id(documents: list[dict]) -> list:
    docs_without_id = []
    for doc in documents:
        doc_without_id = {key: value for key, value in doc.items() if key != '_id'}
        docs_without_id.append(doc_without_id)
    return docs_without_id
