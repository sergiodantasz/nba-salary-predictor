from pathlib import Path

ARTIFACTS_DIR = Path(__file__).resolve().parent.parent / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "model.keras"
PREPROCESSOR_PATH = ARTIFACTS_DIR / "preprocessor.pkl"

SALARY_CAP_HISTORY = {
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
