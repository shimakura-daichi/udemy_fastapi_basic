from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.Contact])
async def get_contact_all():
    dummy_date = datetime.now()
    return [contact_schema.Contact(
        id=1,
        name="John Doe",
        email="john.doe@example.com",
        url="https://example.com/johndoe",
        gender=1,
        message="Hello, World!",
        is_enabled=False,
        created_at=dummy_date)]

@router.get("/contacts/{contact_id}", response_model=contact_schema.Contact)
async def get_contact(contact_id: int):
    return contact_schema.contact(id)

@router.post("/contacts", response_model=contact_schema.Contact)
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.put("/contacts/{contact_id}", response_model=contact_schema.Contact)
async def update_contact(contact_id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{contact_id}", response_model=contact_schema.Contact)
async def delete_contact(contact_id: int):
    return