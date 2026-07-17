from typing import Annotated

from fastapi import Body, FastAPI, Query

from app.schemas import Player, PredictionResponse
from app.services import predict_salary

app = FastAPI()


@app.post("/predict/")
def predict(
    player_stats: Annotated[Player, Body()],
    year: Annotated[int, Query(ge=2017, le=2026)],
) -> PredictionResponse:
    return predict_salary(player_stats, year)
