from fastapi import APIRouter, HTTPException
from model import TaskModel
from app import controller

router = APIRouter()


@router.post('/tasks/')
async def create_task(task: TaskModel):
    res = controller.create_task(task)
    if res:
        return res
    raise HTTPException(status_code=400, detail="Task Insertion Has Been Failed")


@router.get('/tasks/{task_id}')
async def read_task(task_id: int):
    res = controller.read_task(task_id)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Task not found")


@router.put('/tasks/{task_id}')
async def update_task(task_id: int, task: TaskModel):
    res = controller.update_task(task_id, task)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    res = controller.delete_task(task_id)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Task not found")


@router.get('/tasks/')
async def read_all_tasks():
    res = controller.read_all_task()
    if res:
        return res
    raise HTTPException(status_code=404, detail="Internal Error")
