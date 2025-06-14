import cx_Oracle as oci
from faker import Faker
import random

fake = Faker('ko-KR')

sid = 'XE'
host = '210.119.14.71'
port = 1521
username = 'attendance'
password = '12345'

def loadSdata():
    conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
    cursor = conn.cursor()

    query = '''SELECT T_NO, T_ID, T_PW, T_NAME, T_TEL, CLASS_NO
                FROM ATTENDANCE.TEACHER'''
    cursor.execute(query)

    lst_teacher = [item for item in cursor]  

    cursor.close()
    conn.close()

    return lst_teacher


if __name__ == "__main__":
    teacher_data = loadSdata()
    print("loadSdata 실행 결과:", teacher_data)