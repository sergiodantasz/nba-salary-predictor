from typing import Annotated

from fastapi import Body, FastAPI, Query, status

from app.schemas import Player, PredictionResponse
from app.services import predict_salary

app = FastAPI(
    title="NBA Salary Predictor",
    description="Estima o salário de um jogador da NBA com base em estatísticas de desempenho, utilizando uma rede neural profunda treinada com dados históricos de 2017 a 2025.",
    version="1.0.0",
    docs_url="/docs",
)


@app.post(
    "/predict/",
    summary="Estimar salário",
    description="Recebe as estatísticas de um jogador e um ano-alvo, e retorna o salário estimado em dólares, a fração do teto salarial correspondente e o teto utilizado no cálculo.",
    response_description="Salário estimado e metadados da predição",
    status_code=status.HTTP_200_OK,
    tags=["Predição"],
)
def predict(
    player_stats: Annotated[
        Player,
        Body(
            description="Estatísticas do jogador",
            examples=[
                {
                    "Age": 31,
                    "G": 36,
                    "GS": 36,
                    "MP": 28.9,
                    "3P%": 0.333,
                    "eFG%": 0.636,
                    "FT%": 0.650,
                    "TRB": 9.8,
                    "AST": 5.4,
                    "STL": 0.9,
                    "BLK": 0.7,
                    "TOV": 3.2,
                    "PF": 2.4,
                    "PTS": 27.6,
                    "Pos": "PF",
                },
            ],
        ),
    ],
    year: Annotated[
        int,
        Query(
            ge=2017,
            le=2026,
            description="Ano-alvo da predição (teto salarial)",
            examples=[2026],
        ),
    ],
) -> PredictionResponse:
    return predict_salary(player_stats, year)
