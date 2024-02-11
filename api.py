from fastapi import APIRouter
from model import TaskModel

router = APIRouter()


@router.post('/tasks/')
async def create_task(task: TaskModel):
    pass


@router.get('/tasks/{task_id}')
async def read_task(task_id: int):
    pass


@router.put('/tasks/{task_id}')
async def update_task(task_id: int, task: TaskModel):
    pass


@router.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    pass
