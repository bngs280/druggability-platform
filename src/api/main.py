from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():

    return {

        "project":"Druggability AI",
        "status":"running"

    }