from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Сурков Илья Юрьевич"}

@app.get('/tools')
async def f_indexT():
    return "Не программирую!"

@app.get('/users')
async def f_indexU():
    return "+79553265488"