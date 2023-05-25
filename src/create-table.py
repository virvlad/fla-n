from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/script/')
def script():
       
    db_host = "db"
    db_port = "5432"
    db_name = "postgres"
    db_user = "postgres"
    db_password = "postgres"

    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
)

    cur = conn.cursor()

    cur.execute("""
    
        CREATE TABLE mytable (
            id SERIAL PRIMARY KEY,
            number INTEGER,
            factorial INTEGER
        );

         INSERT INTO mytable (number, factorial) VALUES
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120);       

    """)

    conn.commit()

    cur.close()
    conn.close()

    return '<H1> TABLE <i>mytable</i> has been created  </H1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
