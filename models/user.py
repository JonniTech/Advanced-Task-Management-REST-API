from tortoise import fields,models
from models.project import Project
from models.task import Task

class User(models.Model):
    id =  fields.IntField(pk=True)
    username = fields.CharField(max_length=50,unique=True)
    email = fields.CharField(max_length=255,unique=True)
    password = fields.CharField(max_length=255)
    role = fields.CharField(max_length=20,default="user")

    projects =  fields.ReverseRelation["Project"] #projects of this user
    tasks_assigned = fields.ManyToManyRelation["Task"]  # task assigned to this user

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"