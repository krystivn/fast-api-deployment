from fastapi import APIRouter, HTTPException
from repository import NoteRepository

from schema import NoteCreate, ResponseSchema
from model import Note
from typing import List

router = APIRouter(
    prefix="/note",
    tags=['note']
)


@router.post("", response_model=ResponseSchema[None], response_model_exclude_none=True)
async def create_note(create_form: NoteCreate):
    await NoteRepository.create(create_form)
    return ResponseSchema(detail="Successfully created data!")

@router.get("", response_model=ResponseSchema[List[Note]], response_model_exclude_none=True)
async def get_all_note():
    try:
        data = await NoteRepository.get_all()
        return ResponseSchema(detail="Successfully fetched data!", result=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))