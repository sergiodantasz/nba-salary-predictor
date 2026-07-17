from enum import Enum

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class Position(str, Enum):
    CENTER = "C"
    POWER_FORWARD = "PF"
    POINT_GUARD = "PG"
    SMALL_FORWARD = "SF"
    SHOOTING_GUARD = "SG"


class Player(BaseModel):
    model_config = {"validate_by_name": True}

    age: int = Field(ge=18, le=50, alias="Age")
    games_played: int = Field(ge=10, le=82, alias="G")
    games_started: int = Field(ge=0, le=82, alias="GS")
    minutes_per_game: float = Field(ge=5, le=60, alias="MP")
    three_point_pct: float = Field(ge=0, le=1, alias="3P%")
    efg_pct: float = Field(ge=0, le=1.5, alias="eFG%")
    ft_pct: float = Field(ge=0, le=1, alias="FT%")
    total_rebounds: float = Field(ge=0, le=40, alias="TRB")
    assists: float = Field(ge=0, le=35, alias="AST")
    steals: float = Field(ge=0, le=15, alias="STL")
    blocks: float = Field(ge=0, le=20, alias="BLK")
    turnovers: float = Field(ge=0, le=15, alias="TOV")
    personal_fouls: float = Field(ge=0, le=10, alias="PF")
    points: float = Field(ge=0, le=100, alias="PTS")
    position: Position = Field(alias="Pos")

    @field_validator("games_started")
    @classmethod
    def games_started_must_not_exceed_games_played(
        cls, value: int, info: ValidationInfo
    ) -> int:
        if value > info.data.get("games_played", 0):
            raise ValueError("games_started cannot exceed games_played")
        return value


class PredictionResponse(BaseModel):
    predicted_salary: float = Field(ge=0)
    salary_cap_ratio: float = Field(ge=0, le=1)
    salary_cap: float = Field(ge=0)
    season: str = Field(min_length=7, max_length=7, pattern=r"^\d{4}-\d{2}$")
