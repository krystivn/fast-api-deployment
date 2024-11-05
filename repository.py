from sqlalchemy.sql import select
from schema import NoteCreate
from config import db, commit_rollback
from model import Note



class NoteRepository:

    @staticmethod
    async def create(form: NoteCreate):
        db.add(Note(name=form.name, description=form.description))
        await commit_rollback()

    @staticmethod
    async def get_all():
        query = select(Note)
        result = await db.execute(query)
        return result.scalars().all()

        