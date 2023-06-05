from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from database import get_async_session
from pydantic.types import List
from task.models import task
from task.schemas import TaskCreate, TaskRead

router = APIRouter(
    prefix='/task',
    tags=['tasks']
)


@router.get('/', response_model=List[TaskRead])
async def get_all_tasks(session: AsyncSession = Depends(get_async_session)):
    query = select(task)
    result = await session.execute(query)
    return result.all()

@router.get('/{task_id}', response_model=TaskRead)
async def get_task_by_id(task_id: int, session: AsyncSession=Depends(get_async_session)):
    query = select(task).where(task.c.id == task_id)
    result = await session.execute(query)
    return result.first()

@router.post('/')
async def create_task(new_task: TaskCreate ,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(task).values(**new_task.dict())
    result = await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
    