from fastapi import FastAPI
from view import router
app = FastAPI()
app.include_router(router)

@app.get("/", tags=["Based"])
def main():
    return "Hello world!"


if __name__ == '__main__':
    main()
