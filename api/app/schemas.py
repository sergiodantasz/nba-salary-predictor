from enum import Enum

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class Position(str, Enum):
    """
    Posição em quadra do jogador.
    """

    CENTER = 'C'
    POWER_FORWARD = 'PF'
    POINT_GUARD = 'PG'
    SMALL_FORWARD = 'SF'
    SHOOTING_GUARD = 'SG'


class Player(BaseModel):
    """
    Estatísticas de desempenho de um jogador da NBA.

    Os campos seguem as abreviações padrão da liga, acessíveis também pelos aliases originais (ex: ``games_played`` ou ``G``).
    """

    model_config = {'validate_by_name': True}

    age: int = Field(ge=18, le=50, alias='Age', description='Idade do jogador')
    games_played: int = Field(ge=10, le=82, alias='G', description='Jogos disputados na temporada')
    games_started: int = Field(ge=0, le=82, alias='GS', description='Jogos como titular')
    minutes_per_game: float = Field(ge=5, le=60, alias='MP', description='Minutos por jogo')
    three_point_pct: float = Field(ge=0, le=1, alias='3P%', description='Percentual de cestas de 3 pontos')
    efg_pct: float = Field(ge=0, le=1.5, alias='eFG%', description='Effective field goal percentage')
    ft_pct: float = Field(ge=0, le=1, alias='FT%', description='Percentual de lances livres')
    total_rebounds: float = Field(ge=0, le=40, alias='TRB', description='Rebotes por jogo')
    assists: float = Field(ge=0, le=35, alias='AST', description='Assistências por jogo')
    steals: float = Field(ge=0, le=15, alias='STL', description='Roubos de bola por jogo')
    blocks: float = Field(ge=0, le=20, alias='BLK', description='Tocos por jogo')
    turnovers: float = Field(ge=0, le=15, alias='TOV', description='Turnovers por jogo')
    personal_fouls: float = Field(ge=0, le=10, alias='PF', description='Faltas pessoais por jogo')
    points: float = Field(ge=0, le=100, alias='PTS', description='Pontos por jogo')
    position: Position = Field(alias='Pos', description='Posição em quadra')

    @field_validator('games_started')
    @classmethod
    def games_started_must_not_exceed_games_played(cls, value: int, info: ValidationInfo) -> int:
        if value > info.data.get('games_played', 0):
            raise ValueError('games_started cannot exceed games_played')
        return value


class PredictionResponse(BaseModel):
    """
    Resultado da predição salarial.
    """

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'predicted_salary': 58148048,
                    'salary_cap_ratio': 0.376,
                    'salary_cap': 154647000,
                    'season': '2025-26',
                },
            ],
        },
    }

    predicted_salary: float = Field(ge=0, description='Salário estimado em dólares')
    salary_cap_ratio: float = Field(ge=0, le=1, description='Fração do teto salarial (0–1)')
    salary_cap: float = Field(ge=0, description='Teto salarial do ano utilizado no cálculo')
    season: str = Field(
        min_length=7,
        max_length=7,
        pattern=r'^\d{4}-\d{2}$',
        description='Temporada correspondente (ex: 2025-26)',
    )
