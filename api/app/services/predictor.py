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


def predict_salary(player: Player, year: int) -> PredictionResponse:
    df = pd.DataFrame([player.model_dump(by_alias=True)])
    X = _preprocessor.transform(df)

    log_pred = _model.predict(X, verbose="0")
    salary_pct = float(np.expm1(log_pred[0][0]))
    salary = round(salary_pct * SALARY_CAP_HISTORY[year])

    return PredictionResponse(salary_pct=salary_pct, salary=salary)
