from fastapi import HTTPException,status,APIRouter,Depends
from api.v1.routes.auth_routes import get_current_user
from services.project_services import ProjectService
from schemas.project_schemas import ProjectCreate,ProjectUpdate,ProjectOut
from models.user import User

router = APIRouter(prefix="/api/projects",tags=["Projects"])

@router.post("/",response_model=ProjectOut,status_code=status.HTTP_201_CREATED)
async def create_project(payload:ProjectCreate,current_user:User = Depends(get_current_user)):
    project = await ProjectService.create_project(payload,current_user.id)
    return project

@router.get("/",status_code=status.HTTP_200_OK)
async def get_current_user_projects(current_user:User = Depends(get_current_user)):
    projects = await ProjectService.get_user_projects(current_user.id)
    return projects

@router.get("/{project_id}",response_model=ProjectOut,status_code=status.HTTP_200_OK)
async def get_single_product(project_id:int,current_user:User = Depends(get_current_user)):
    project =  await ProjectService.get_project_by_id(project_id,current_user.id)

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Project not found")
    
    return project

@router.put("/{project_id}",response_model=ProjectOut,status_code=status.HTTP_200_OK)
async def update_project(project_id:int,payload:ProjectUpdate,current_user:User = Depends(get_current_user)):
    project = await ProjectService.update_project(project_id,payload,current_user.id)

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Project not found")
    
    return project

@router.delete("/{project_id}",status_code=status.HTTP_200_OK)
async def delete_project(project_id:int,current_user:User = Depends(get_current_user)):
    deleted = await ProjectService.delete_project(project_id,current_user.id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Project not found")
    
    return {"message":"Product deleted successfully"}