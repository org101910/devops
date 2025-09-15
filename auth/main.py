from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/auth")
async def auth(request: Request):
    """
    Simple auth endpoint for Nginx auth_request.
    Always returns 200 OK.
    """
    return RedirectResponse(url="https://www.google.com", status_code=302)
    # not authenticated:
    return Response(status_code=401)
    # not authorised:
    return Response(status_code=403)