import pymysql
import pandas as pd
from sqlalchemy.sql import text
from sqlalchemy import create_engine


def getdata_from_db(value):
    # 데이터베이스 연결
    try:
        engine = create_engine('mysql+pymysql://new_user:1234@192.168.0.187:3306/test')
        #engine = create_engine('mysql+pymysql://root:1234@localhost/test') 내 로컬
        with engine.begin() as con:
            print("Database connection successful.")
            # 데이터 삽입 쿼리 실행
            query = text(f'INSERT INTO test.company (ID) VALUES ("{value}")')
            #query = text(f'INSERT INTO test.com (설립연도) VALUES ("{value}")')내 로컬
            con.execute(query)
            print(f"Value '{value}' inserted successfully into ID.")
    except Exception as e:
        print("An error occurred while inserting data:", e)

def main():
    value = '박일광'
    df = getdata_from_db(value)
    
    if df is not None:
        print(df)
        print(f"Number of records: {len(df)}")

if __name__ == '__main__':
    main()