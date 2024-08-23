import os
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
	return {"message":"Helloooooooooow"}

@app.get("/variables")
async def variables():
	variables = dict()
	variables['version'] = os.environ.get('APP_VERSION')
	variables['token'] = os.environ.get('TOKEN')
	return {'variables': variables}
