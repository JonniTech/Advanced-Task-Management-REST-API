from tortoise import models,fields
from models.task import Task

class Project(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    owner = fields.ForeignKeyField("models.User", related_name="projects")
    tasks = fields.ReverseRelation["Task"]  # tasks under this project
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "projects"

    def __str__(self):
        return self.name