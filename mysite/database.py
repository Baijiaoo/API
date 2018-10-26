# -*- coding:utf-8 -*-
import json
import sqlite3

def insert(conn, agent_id, observe_score, evaluate_score, predict_score):
	sql_insert = '''
	INSERT INTO
	agent_score(agent_id, observe_score, evaluate_score, predict_score)
	VALUES
	(?,?,?,?);
	'''
	conn.execute(sql_insert,(agent_id, observe_score, evaluate_score, predict_score))
	print ('Insert Successfully')
	
	
def main():
	db_path = 'agent_score.db'
	json_path = 'model/result.json'
	conn = sqlite3.connect(db_path)
	print ('Open Database')
	
	with open(json_path, 'r') as load_f:
		data = json.load(load_f)

		for line in data['Data']:
			insert(conn, line['ID'],line['Observe'], line['Evaluate'], line['Predict'])
			conn.commit()
			print (line['ID'])
	conn.close()

if __name__ == '__main__':
	main()
