from fastapi import FastAPI

#instance of FASTAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message":  "Hello World"}