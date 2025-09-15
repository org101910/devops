from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/auth")
async def auth(request: Request):
    """
    Simple auth endpoint for Nginx auth_request.
    Always returns 200 OK.
    """
    return Response(status_code=200)