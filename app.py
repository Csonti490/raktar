from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello raktár!"

if __name__ == "__main__":
    app.run(debug=True)

def init_db():
if not os.path.exists("raktar.db"):
    conn = get_db_connection()
    with open("raktar.sql", "r", encoding="utf8") as f:
            conn.executescript(f.read())
    conn.commit()
    conn.close()

init_db()