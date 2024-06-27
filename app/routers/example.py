from fastapi import APIRouter
from models.example_model import Example

router = APIRouter(prefix="/example", tags=["example"])


@router.get("/{example_id}")
async def get_basic_example(example_id: str):
    return {
        "property1": "value1",
        "property2": ["va1", "val2"],
        "id": example_id
    }


@router.post("/")
async def create_new_example(example: Example):
    return example
