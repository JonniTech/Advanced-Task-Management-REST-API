from models.task import Task
from schemas.task_schemas import TaskCreate, TaskUpdate
from models.user import User 
from tortoise.expressions import Q

# Service class for managing tasks with many to many relationship with users

class TaskService:

    @staticmethod
    async def create_task(data: TaskCreate, owner_id: int):
        task = await Task.create(
            title=data.title,
            description=data.description,
            owner_id=owner_id
        )

        # Assign task to users if provided
        if hasattr(data, 'assigned_to_ids') and data.assigned_to_ids:
            users = await User.filter(id__in=data.assigned_to_ids).all()

            if len(users) != len(data.assigned_to_ids):
               return None
            
            await task.assigned_to.add(*users)
        
        return task
    
    @staticmethod
    async def get_user_task(user_id:int):
        tasks =  await Task.filter(
            (Q(assigned_to__id=user_id) | Q(owner_id=user_id))
        ).distinct()

        return tasks
    
    @staticmethod
    async def get_task_by_id(task_id:int,user_id:int):
        task = await Task.filter(
            Q(id=task_id) & 
            (Q(assigned_to__id=user_id) | Q(owner_id=user_id))
        ).first()
        return task
    
    #only owner can update the task
    @staticmethod
    async def update_task(task_id:int,data:TaskUpdate,owner_id:int):
        task =  await Task.filter(id=task_id,owner_id=owner_id).first()

        if not task:
            return None
        
        if data.title is not None:
            task.title =  data.title
        
        if data.description is not None:
            task.description = data.description

        if data.completed is not None:
            task.completed = data.completed

        if data.assigned_to is not None:
            users = await User.filter(id__in=data.assigned_to).all()

            if len(users) != len(data.assigned_to):
               return None
            
            await task.assigned_to.clear()
            await task.assigned_to.add(*users)

        await task.save()
        return task
    
    @staticmethod
    async def delete_task(task_id:int,owner_id:int):
        task = await Task.filter(id=task_id,owner_id=owner_id).first()

        if not task:
            return False
        
        await task.delete()
        return True