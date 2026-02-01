from fastapi import FastAPI, APIRouter

doc_ai = APIRouter(prefix="/api/doc-ai")


@doc_ai.get("/")
async def greet():
    return "Hello World!"



app = FastAPI(
    title="Doc AI"
)

app.include_router(doc_ai)
