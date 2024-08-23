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
	variables['bancodev'] = os.environ.get('BANCODEV')
	variables['config'] = open('/app/config-dev.yml', 'r').read()
	return {'variables': variables}
