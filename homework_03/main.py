from fastapi import FastAPI, Response
import json

app = FastAPI()


@app.get("/")
def main():
    return "Hello world!"


@app.get("/ping/")
def ping():
    return Response(content=json.dumps({"message": "pong"}), status_code=200, media_type="application/json")


if __name__ == '__main__':
    main()
