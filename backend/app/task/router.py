from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import select, insert
from task.models import Task
from task.scemas import TaskCreate

router = APIRouter(
    prefix='/task',
    tags=['Task']
)


@router.post('')
async def create_task(new_task: TaskCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Task).values(**new_task.__dict__)
    await session.execute(stmt)
    await session.commit()
    print(new_task.__dict__)
    return {"status": "success"}


@router.get('')
async def get_tasks(session: AsyncSession = Depends(get_async_session)):
    query = select(Task)
    result = await session.execute(query)
    return result.all()

@router.get('/{id}')
async def get_task_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Task).where(Task.id == id)
    result = await session.execute(query)
    return result.first()