import sortdata
import sqlite3
import os


if os.path.exists("chinese.db"):
    raise RuntimeError("Target file already exists.")


with sqlite3.connect("chinese.db") as db:
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE chars (
        code INTEGER PRIMARY KEY,
        strokes INTEGER NOT NULL,
        freq INTEGER NOT NULL
    );""")

    for code, info in sortdata.data.items():
        cursor.execute("INSERT INTO chars (code, strokes, freq) VALUES (?, ?, ?)",
                       [code, info["kTotalStrokes"], info["kFrequency"]])

    db.commit()
