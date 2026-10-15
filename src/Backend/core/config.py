from pathlib import Path
from dotenv import dotenv_values

# anchor to the project root (src/Backend/core/../../../.env) regardless of the current working directory
ENV_PATH = Path(__file__).resolve().parents[3] / ".env"
config = dotenv_values(ENV_PATH)

DB_HOST = config["DB_HOST"]
DB_PORT = config["DB_PORT"]
DB_NAME = config["DB_NAME"]
DB_USER = config["DB_USER"]
DB_PASSWORD = config["DB_PASSWORD"]

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
