from enum import Enum
from typing import Annotated, cast

import numpy as np
import pandas as pd
from fastapi import Body, FastAPI, Query
from joblib import load
from keras import Model
from keras.models import load_model
from pydantic import BaseModel, Field, ValidationInfo, field_validator
from sklearn.compose import ColumnTransformer

app = FastAPI()

model = cast(Model, load_model("artifacts/model.keras"))
preprocessor: ColumnTransformer = load("artifacts/preprocessor.pkl")

salary_cap_history = {
    2017: 94_143_000,
    2018: 99_093_000,
    2019: 101_869_000,
    2020: 109_140_000,
    2021: 109_140_000,
    2022: 112_414_000,
    2023: 123_655_000,
    2024: 136_021_000,
    2025: 140_588_000,
    2026: 154_647_000,
}


class Position(str, Enum):
    CENTER = "C"
    POWER_FORWARD = "PF"
    POINT_GUARD = "PG"
    SMALL_FORWARD = "SF"
    SHOOTING_GUARD = "SG"


class Player(BaseModel):
    model_config = {"validate_by_name": True}

    age: int = Field(ge=18, le=50, alias="Age")
    g: int = Field(ge=10, le=82, alias="G")
    gs: int = Field(ge=0, le=82, alias="GS")
    mp: float = Field(ge=5, le=60, alias="MP")
    three_pt_pct: float = Field(ge=0, le=1, alias="3P%")
    efg_pct: float = Field(ge=0, le=1.5, alias="eFG%")
    ft_pct: float = Field(ge=0, le=1, alias="FT%")
    trb: float = Field(ge=0, le=40, alias="TRB")
    ast: float = Field(ge=0, le=35, alias="AST")
    stl: float = Field(ge=0, le=15, alias="STL")
    blk: float = Field(ge=0, le=20, alias="BLK")
    tov: float = Field(ge=0, le=15, alias="TOV")
    pf: float = Field(ge=0, le=10, alias="PF")
    pts: float = Field(ge=0, le=100, alias="PTS")
    pos: Position = Field(alias="Pos")

    @field_validator("gs")
    @classmethod
    def gs_must_not_exceed_g(cls, value: int, info: ValidationInfo) -> int:
        if value > info.data.get("g", 0):
            raise ValueError("gs cannot be greater than g")
        return value


class Response(BaseModel):
    salary_pct: float = Field(ge=0, le=1)
    salary: float = Field(ge=0)


@app.post("/predict/")
def predict(
    player_stats: Annotated[Player, Body()],
    year: Annotated[int, Query(ge=2017, le=2026)],
):
    df = pd.DataFrame([player_stats.model_dump(by_alias=True)])
    X = preprocessor.transform(df)

    log_pred = model.predict(X, verbose="0")
    salary_pct = float(np.expm1(log_pred[0][0]))
    salary = round(salary_pct * salary_cap_history[year])

    return Response(salary_pct=salary_pct, salary=salary)
