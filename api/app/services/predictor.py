from typing import cast

import numpy as np
import pandas as pd
from joblib import load
from keras import Model
from keras.models import load_model
from sklearn.compose import ColumnTransformer

from app.config import MODEL_PATH, PREPROCESSOR_PATH, SALARY_CAP_HISTORY
from app.schemas import Player, PredictionResponse

_model: Model = cast(Model, load_model(MODEL_PATH))
_preprocessor: ColumnTransformer = load(PREPROCESSOR_PATH)


def _format_season(year: int) -> str:
    return f'{year - 1}-{str(year)[-2:]}'


def predict_salary(player: Player, year: int) -> PredictionResponse:
    df = pd.DataFrame([player.model_dump(by_alias=True)])
    X = _preprocessor.transform(df)

    log_salary_share = _model.predict(X, verbose='0')
    salary_cap_ratio = float(np.expm1(log_salary_share[0][0]))
    salary_cap = SALARY_CAP_HISTORY[year]
    predicted_salary = round(salary_cap_ratio * salary_cap)

    return PredictionResponse(
        predicted_salary=predicted_salary,
        salary_cap_ratio=salary_cap_ratio,
        salary_cap=salary_cap,
        season=_format_season(year),
    )
