from tortoise import Tortoise
from configs.settings import DATABASE_URL

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={
            "models":["models.user","models.task","models.project"]
        }
    )

    await Tortoise.generate_schemas()