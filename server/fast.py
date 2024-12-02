from fastapi import FastAPI

# from starlette.middleware.cors import CORSMiddleware

# ring_config = get_config()
# app = FastAPI(root_path=ring_config.root_path)
app = FastAPI()

# if ring_config.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[
#             str(origin).strip("/")
#             for origin in ring_config.BACKEND_CORS_ORIGINS
#         ],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# app.include_router(router)
