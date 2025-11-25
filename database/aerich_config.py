from configs.settings import DATABASE_URL

TORTOISE_ORM = {
    "connections": {"default":DATABASE_URL},
    "apps":{
        "models":{
            "models":["models.user","models.task","models.project","aerich.models"],
            "default_connection":"default"
        }
    }
}
