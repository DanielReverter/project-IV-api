from config.sql_config import engine
import pandas as pd

## GET
def get_days ():

    query = (f"""
    SELECT DISTINCT date from tweets
	ORDER BY date desc;
    """)
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_everything_from_day(date):

    query = (f"""SELECT * FROM tweets WHERE date = "{date}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')


## POST
def new_message (date, tweet, language):

    engine.execute(f"""
    INSERT INTO tweets (date, tweet, language)
    VALUES ('{date}', '{tweet}', '{language}');
    """)
    
    return f"Correctly introduced: {date} {tweet} {language}"

def erase_day (date):

    engine.execute(f"""DELETE FROM tweets WHERE date='{date}';""")
    
    return f"Correctly deleted tweets from: {date}"