from flask import Flask, render_template
import pandas as pd
import numpy as np
import mysql.connector
import time

time.sleep(10)

conn = mysql.connector.connect(
    host='db',
    user='user',
    password='userpassword',
    database='titanic_db'
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passengers (
    id INT PRIMARY KEY,
    pclass INT,
    survived INT,
    pname VARCHAR(255),
    sex VARCHAR(10),
    age FLOAT,
    sibsp INT,
    parch INT,
    ticket VARCHAR(50),
    fare FLOAT,
    cabin VARCHAR(50),
    embarked VARCHAR(10),
    boat INT,
    body INT,
    homedest VARCHAR(50)
)
""")

cursor.execute("SELECT COUNT(*) FROM passengers;")
if cursor.fetchone()[0] == 0:
    df = pd.read_csv('my_titanic.csv')
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.astype(object).where(pd.notnull(df), None)
    for _, row in df.iterrows():
        sql = """
        INSERT INTO passengers (id, pclass, survived, pname, sex, age, sibsp, parch, ticket, fare, cabin, embarked, boat, body, homedest)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            row['id'], row['pclass'], row['survived'], row['pname'], row['sex'],
            row['age'], row['sibsp'], row['parch'], row['ticket'], row['fare'],
            row['cabin'], row['embarked'], row['boat'], row['body'], row['homedest']
        )
        cursor.execute(sql, values)
    conn.commit()

cursor.close()
conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host='db',
        user='user',
        password='userpassword',
        database='titanic_db'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM passengers;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
