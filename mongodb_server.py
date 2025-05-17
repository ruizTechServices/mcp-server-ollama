import os
from mcp import FastMCP
from pymongo import MongoClient

server = FastMCP()

client = MongoClient(os.getenv('MONGODB_URI'))
db = client[os.getenv('DATABASE_NAME')]

@server.tool(description="Find MongoDB documents")
def mongodb_find(collection_name: str, filter: dict):
    collection = db[collection_name]
    docs = list(collection.find(filter))
    return {"documents": docs}

server.run()
