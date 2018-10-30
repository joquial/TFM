from datetime import datetime, timedelta
from pymongo import MongoClient, GEO2D
from pymongo.errors import BulkWriteError
import time
import pandas as pd

def _connect_mongo(host, port, username, password, db):

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]
def read_mongo(db, collection, sensor, host='mongodb', port=27017, username=None, password=None, limit_num = None, no_id=True):
    time.sleep(2)
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    today = datetime.now()
    DD = timedelta(days=3)
    Dd = timedelta(days=1)

    earlier = today - DD
    future = today + Dd

    earlier_str = earlier.strftime('%Y%m%d')
    future_str = future.strftime('%Y%m%d')

    year = earlier_str[:4]
    month = earlier_str[4:6]
    day = earlier_str[-2:]
    antdate= day + '/' + month + '/' + year 

    year = future_str[:4]
    month = future_str[4:6]
    day = future_str[-2:]
    postdate= day + '/' + month + '/' + year
    query={'$and' :[  {'date':{'$lt':postdate,'$gt':antdate}}, {'name' : sensor},{'time':{'$lt':'08:20:00','$gt':'08:00:00'}}   ]   }
    if limit_num:
        assert type(limit_num) is int, '@read_mongo: id is not an integer: %r' % id
        cursor = db[collection].find(query).limit(limit_num)
    else:
        cursor = db[collection].find(query)
    df =  pd.DataFrame(list(cursor))

    if no_id:
        del df['_id']

    return df
def read_mongo2(db, collection, sensor, host='mongodb', port=27017, username=None, password=None, limit_num = None, no_id=True):
    time.sleep(2)
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    today = datetime.now()
    DD = timedelta(days=3)
    Dd = timedelta(days=1)

    earlier = today - DD
    future = today + Dd

    earlier_str = earlier.strftime('%Y%m%d')
    future_str = future.strftime('%Y%m%d')

    year = earlier_str[:4]
    month = earlier_str[4:6]
    day = earlier_str[-2:]
    antdate= day + '/' + month + '/' + year 

    year = future_str[:4]
    month = future_str[4:6]
    day = future_str[-2:]
    postdate= day + '/' + month + '/' + year
    query={'$and' :[  {'date':{'$lt':postdate,'$gt':antdate}}, {'name' : sensor},{'time':{'$lt':'19:20:00','$gt':'19:00:00'}}   ]   }
    if limit_num:
        assert type(limit_num) is int, '@read_mongo: id is not an integer: %r' % id
        cursor = db[collection].find(query).limit(limit_num)
    else:
        cursor = db[collection].find(query)
    df =  pd.DataFrame(list(cursor))

    if no_id:
        del df['_id']

    return df
def insert_mongo(db, collection, data, host='mongodb', port=27017, username=None, password=None):
    
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)
    
    try:
        res = db[collection].insert_many(data)
    except BulkWriteError as bwe:
        print bwe.details
        raise

    return res
