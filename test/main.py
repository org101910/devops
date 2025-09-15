from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
async def index(request: Request):
    """
    Always returns 200 OK.
    """
    return Response(content="Hello World!",status_code=200)