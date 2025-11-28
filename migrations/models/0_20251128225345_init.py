from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "role" VARCHAR(20) NOT NULL DEFAULT 'user',
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "projects" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "owner_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "tasks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "completed" BOOL NOT NULL DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "owner_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "project_id" INT NOT NULL REFERENCES "projects" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "tasks_users" (
    "tasks_id" INT NOT NULL REFERENCES "tasks" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_tasks_users_tasks_i_e4bab8" ON "tasks_users" ("tasks_id", "user_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmm1v2joUx78KyqteiU0bt2zT3kFL79gKTG26TZumyCRuyCWxM8cZRRPffbYT58F5GG"
    "mhF3rzpoXjcxKfn+3Y/xN+aR62oBs8/0jwv9Ck2tvOLw0BD7IPalO3owHfTxu4gYK5K3z9"
    "yEkYwTygBIiL3QI3gMxkwcAkjk8djJgVha7Ljdhkjg6yU1OInB8hNCi2IV1Awhq+fWdmB1"
    "nwDgbyq780bh3oWrneOha/t7AbdO0L2xjRC+HI7zY3TOyGHkqd/TVdYJR4O0gkaUMECaCQ"
    "X56SkHef9y7OVGYU9TR1ibqYibHgLQhdmkl3SwYmRpwf600gErT5XZ71Xp6+Pn3z96vTN8"
    "xF9CSxvN5E6aW5R4GCwFTXNqIdUBB5CIwpN/G/QO5sAUg5OumvwGNdVuFJVHX0pCHFl06Z"
    "HfHzwJ3hQmTTBfv68sWLGlqfBldn7wZXJ8zrL54NZtM4mt/TuKkXtXGkKcJszwokdXhXMQ"
    "mVsHsBjSfbI/KswaePvui8z14Q/HCz1E4mgy8CqLeOWy5n03+ke4by2eVsqMA1CeTpG4AW"
    "2Z6zFup4sJxvPlLBa8Whz+WHA529LAdrhtx1PNZ19MeT0bU+mHzMDcH5QB/xll4Ov7SevF"
    "LmeXKRzuex/q7Dv3a+zqYjQRAH1Cbijqmf/lXjfQIhxQbCKwNYmWegtEowuYENfeueA5uP"
    "bAf2Px3YuPPpuOIVY2002o6zIX/elA9kAHewL/PDzO2ydFsWSIoILzCBjo0+wLUgOWZdAs"
    "gs25Dj09tNAA90Y97IWSCt6fQiYJWc8HKTg+XHsoI0OqMMrs8G5yNNYJwDc7kCxDIqeFIQ"
    "LIMiz2EcdvHhCrqgYiuOUersEseFUpDBPZwhkmNVbPJ6nmoBCNii1/ze/E5ZHCV6QWKqFg"
    "vJWLRK4dCeSN0apUAd6jaSCklAqxVarfAoWgF7Pt8dShb4EGMXAlShFLJxCts5C9zXbG36"
    "0Nse73A2u8zhHY5VfjeT4YhNX8GaOTnRpiofA60Ae2Ln9FaAPdGBbQXYQ447Kba4hN0MXD"
    "7o/4Su1a470a4lM3AH5DLvbI4XXn5tNZX+D5S+6aiAIGDs2W5HcXFkJgCtdcz/7nlO71s8"
    "1gyK6LmhqHyZB+FlEwYnV2cxJDMBDBNBfAnX4uwQJCsiGYy4KYqN2uiC4NBepGYeF1ROBG"
    "Y3Ckg3tfULkUFJ/UJmVl2/SLrS1i8ObVfq1tQv+LA1fduZjdlNFWPvFHM1jP42JYx+dQWj"
    "XyhgQA84bhOEScAx8uv1+1sAZF6VBEWbctJkj8cVJiXLuJpiNuY4y2l7QUlws5Kk9H88hO"
    "IRou0M4jbruVe9nnuF9dyWd55EFaAt7zzRgU3e4xXUzZ9eeWZ/k3f/t55HKSVzCyHSDxVF"
    "ifYF8HYquETXPUwI3xfmoQlhmYcqhNWyQV4FZ6WuKoMzCvmBKjiZApUieACJYy60Ehkct3"
    "TrhDBIfVolvMvNa89K+CebRKUvoKsPzpmQVn6ktUG2NBpAjN2PE+Befg7B7kghKjmhvr+e"
    "Tate1ichCsgbxBL8Zjkm7XZcJ6DfDxNrDUWede4UWvhVhPoDCOV4yS8wLHs7s7dCecn2sv"
    "kNlec3ig=="
)
