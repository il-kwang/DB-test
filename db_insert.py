import pandas as pd
from sqlalchemy import create_engine


def insert_to_db(csv_file_path):
    # 데이터베이스 연결
    engine = create_engine('mysql+pymysql://root:1234@localhost/test') 

    try:
        # CSV 파일 읽기
        df = pd.read_csv(csv_file_path, header=None)
        df.columns = ['ID', '설립연도', '국가', '분야', '투자단계', '직원 수', '인수여부', '상장여부', 
                      '고객수(백만명)', '총 투자금(억원)', '연매출(억원)', 'SNS 팔로워 수(백만명)', 
                      '기업가치(백억원)', '성공확률']
        
        # 데이터 삽입
        df.to_sql(name='com', con=engine, if_exists='append', index=False)
        print("Data inserted successfully.")
        
    except FileNotFoundError:
        print(f"CSV 파일을 찾을 수 없습니다: {csv_file_path}")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    # CSV 파일 경로
    csv_file = 'C:/Users/302/Documents/미래융합교육원/DB-test/train.csv'
    insert_to_db(csv_file)