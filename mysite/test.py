import json
import sqlite3

JSON_FILE = "result.json"
DB_FILE = "agent_score.db"

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

c.execute('DROP TABLE agent_score_agent_score')

conn.commit()
conn.close()