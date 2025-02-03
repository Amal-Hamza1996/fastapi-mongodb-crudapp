from fastapi import FastAPI
from routes.student import student_router


#create app
app = FastAPI()

#register routers
app.include_router(student_router)
