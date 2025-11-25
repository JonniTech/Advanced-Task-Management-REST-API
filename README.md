# Advanced Task Management API — Enterprise Skeleton (Updated for UV Package Manager)
# (We will expand file-by-file with full explanations)

# Folder Structure Preview (including schemas + versioning)
# Using UV package manager

# app/
#   api/
#     v1/
#       routes/
#         auth_routes.py
#         task_routes.py
#       controllers/
#         auth_controller.py
#         task_controller.py
#
#   auth/
#     hashing.py
#     tokens.py
#     auth_service.py
#
#   configs/
#     settings.py
#
#   database/
#     connection.py
#
#   models/
#     user.py          # Database models ONLY
#     task.py
#
#   schemas/
#     auth_schemas.py  # Pydantic schemas (request/response validation)
#     task_schemas.py
#
#   services/
#     user_service.py
#     task_service.py
#
#   utils/
#     exceptions.py
#     responses.py
#     background.py  # for background task utilities
#
#   main.py

# Notes:
# - models/ folder is strictly for database models.
# - schemas/ folder is strictly for Pydantic schemas (validation & serialization).
# - We are using UV package manager for project dependency management and environment isolation.
# - Project is ready for advanced features like background tasks, JWT refresh tokens, RBAC, and enterprise folder structure.
