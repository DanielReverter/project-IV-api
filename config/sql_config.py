import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()

passw = os.getenv("pass_sql")
dbName = "tesla_tweets"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)