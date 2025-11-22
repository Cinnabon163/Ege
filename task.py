from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE="database.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value TEXT)')
        conn.commit()


@app.route('/add', methods=['POST'])
def add_value():
    data = request.get_json()
    value = data.get('value')
    if not value:
        return jsonify({'error': 'Нет значения'}), 400
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO items (value) VALUES (?)', (value,))
        conn.commit()
    return jsonify({'status': 'success', 'id': c.lastrowid})

@app.route('/values', methods=['GET'])
def get_values():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('SELECT id, value FROM items')
        items = [{'id': row[0], 'value': row[1]} for row in c.fetchall()]
    return jsonify(items)

if __name__ == "__main__":
    init_db()
    app.run()
