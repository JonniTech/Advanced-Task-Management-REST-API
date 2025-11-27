from models.project import Project
from schemas.project_schemas import ProjectCreate,ProjectUpdate

class ProjectService:

    @staticmethod
    async def create_project(data:ProjectCreate,user_id:int):
        project = await Project.create(
            name=data.name,
            description=data.description,
            owner_id=user_id
        )

        return project
    
    @staticmethod
    async def get_user_projects(user_id:int):
        projects =  await Project.filter(owner_id=user_id).all()
        return projects
    
    @staticmethod
    async def get_project_by_id(project_id:int,user_id:int):
        project = await Project.filter(id=project_id,owner_id=user_id).first()
        return project
    
    @staticmethod
    async def update_project(project_id:int,data:ProjectUpdate,user_id:int):
        project =  await Project.filter(id=project_id,owner_id=user_id).first()

        if not project:
            return None
        
        if data.name is not None:
            project.name =  data.name
        
        if data.description is not None:
            project.description = data.description

        await project.save()
        return project
    
    @staticmethod
    async def delete_project(project_id:int,user_id:int):
        project = await Project.filter(id=project_id,owner_id=user_id).first()

        if not project:
            return False
        
        await project.delete()