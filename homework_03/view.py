from fastapi import APIRouter, Response
import json


router = APIRouter(tags=["Ping"])


@router.get("/ping/", tags=["Ping"])
def ping():
    """
    Путь /ping/
    статус ответа 200
    тело ответа — JSON объект {"message": "pong"}
    """
    return Response(content=json.dumps({"message": "pong"}), status_code=200, media_type="application/json")
