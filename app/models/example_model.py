from pydantic import BaseModel


class Example(BaseModel):
    name: str
    description: str | None = None