from fastapi import HTTPException,status,APIRouter,Depends
from api.v1.routes.auth_routes import get_current_user
from services.task_services import TaskService
from schemas.task_schemas import TaskCreate,TaskUpdate,TaskOut
from typing import List
from models.user import User

#only authenticated users can access these routes
#user can see only tasks assigned to them or created by them
#user can create tasks and assign to other users on the project they own only
#user can update or delete only tasks they own

router = APIRouter(prefix="/api/tasks",tags=["Tasks"])

@router.post("/",response_model=TaskOut,status_code=status.HTTP_201_CREATED)
async def create_task(payload:TaskCreate,current_user:User = Depends(get_current_user)):
    task = await TaskService.create_task(payload,current_user.id)

    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="One or more assigned users are invalid")
    
    return task


@router.get("/",status_code=status.HTTP_200_OK)
async def get_current_user_tasks(current_user:User = Depends(get_current_user)):
    tasks = await TaskService.get_user_task(current_user.id)
    return tasks

@router.get("/{task_id}",response_model=TaskOut,status_code=status.HTTP_200_OK)
async def get_single_task(task_id:int,current_user:User = Depends(get_current_user)):
    task =  await TaskService.get_task_by_id(task_id,current_user.id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    
    return task

@router.put("/{task_id}",response_model=TaskOut,status_code=status.HTTP_200_OK)
async def update_task(task_id:int,payload:TaskUpdate,current_user:User = Depends(get_current_user)):
    task = await TaskService.update_task(task_id,payload,current_user.id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    
    return task

@router.delete("/{task_id}",status_code=status.HTTP_200_OK)
async def delete_task(task_id:int,current_user:User = Depends(get_current_user)):
    deleted = await TaskService.delete_task(task_id,current_user.id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    
    return {"message":"Task deleted successfully"}

