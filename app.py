from fastapi import FastAPI, Response
from starlette.requests import Request
from tortoise.contrib.fastapi import register_tortoise
from db_config import TORTOISE_ORM
from messages.routes import router as msg_router

app = FastAPI()

app.include_router(msg_router)

register_tortoise(
    app,
    config=TORTOISE_ORM
)


@app.middleware("http")
async def log_request_response(request: Request, call_next):
    print("request query params:", request.query_params)
    raw_request_body = await request.body()
    print("request body:", raw_request_body)
    await set_body(request, raw_request_body)
    response = await call_next(request)
    body = b""
    if 200 <= response.status_code < 300:
        async for chunk in response.body_iterator:
            body += chunk
        print("response body:", body)
        return Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
    return response


async def set_body(request: Request, body: bytes) -> None:
    async def receive():
        return {'type': 'http.request', 'body': body}

    request._receive = receive
