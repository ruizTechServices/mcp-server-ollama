import os
from mcp import FastMCP
import pinecone

server = FastMCP()

pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENV'))
index = pinecone.Index(os.getenv('PINECONE_INDEX_NAME'))

@server.tool(description="Search Pinecone vectors")
def pinecone_search(query_vector: list, top_k: int):
    results = index.query(vector=query_vector, top_k=top_k)
    return {"matches": results.matches}

server.run()
