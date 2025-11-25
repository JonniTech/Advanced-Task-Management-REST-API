from tortoise import fields, models

class Task(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    completed = fields.BooleanField(default=False)

    project = fields.ForeignKeyField("models.Project", related_name="tasks")
    assigned_to = fields.ManyToManyField("models.User", related_name="tasks_assigned")

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "tasks"