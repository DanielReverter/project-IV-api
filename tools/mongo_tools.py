from config.mongo_config import db, c

## GET
def all_sentences (date):
    query = {"date": f"{date}"}
    sent = list(c.find(query, {"_id": 0})) 
    return sent

## POST
def inserting (dict_):
    c.insert_one(dict_)
    return f"I inserted {dict_} into the db"