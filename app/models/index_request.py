from pydantic import BaseModel


class IndexRequest(BaseModel):
    index: int