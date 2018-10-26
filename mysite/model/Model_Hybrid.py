import tensorflow as tf
from tensorflow.contrib.timeseries.python.timeseries import NumpyReader
from tensorflow.contrib.timeseries.python.timeseries import estimators as ts_estimators

import numpy as np
import json
from copy import deepcopy
import matplotlib.pyplot as plt

from PCA import pca
import TSLM as TS
import warnings
warnings.filterwarnings('ignore')

def model_h(data):
    data_group = data.reset_index(drop=True)
    data_ = {
                tf.contrib.timeseries.TrainEvalFeatures.TIMES: np.array(data_group.index),
                tf.contrib.timeseries.TrainEvalFeatures.VALUES: np.array(data_group.values)
            }
    reader = NumpyReader(data_)
    train_input_fn = tf.contrib.timeseries.RandomWindowInputFn(reader, batch_size=data_group.shape[0], window_size=10)
    LSTM = ts_estimators.TimeSeriesRegressor(model=TS._LSTMModel(num_features=1, num_units=128), optimizer=tf.train.AdamOptimizer(0.001))
    LSTM.train(input_fn=train_input_fn, steps=500)

    evaluation_input_fn = tf.contrib.timeseries.WholeDatasetInputFn(reader)
    evaluation = LSTM.evaluate(input_fn=evaluation_input_fn, steps=3)

    (predictions,) = tuple(LSTM.predict(input_fn=tf.contrib.timeseries.predict_continuation_input_fn(evaluation, steps=5)))

    observed_times = evaluation["times"][0]
    observed = evaluation["observed"][0, :, :]
    evaluated_times = evaluation["times"][0]
    evaluated = evaluation["mean"][0]
    predicted_times = predictions['times']
    predicted = predictions["mean"]

    return observed, evaluated, predicted


_ = pca()
data = _.start()
group_id = data.Group_ID.unique()
jsn_dict= {}
jsn_Dict = {}
jsn_Dict['Data'] = []

for i in group_id:
    tf.reset_default_graph()
    obsList = []
    evaList = []
    preList = []
    data_group = data[data.Group_ID == i]['Grade']

    if data_group.shape[0] > 50:
        o, e, p = model_h(data_group)
        for o_ in o:
            obsList.append(o_[0])
        for e_ in e:
            evaList.append(e_[0])
        for p_ in p:
            preList.append(p_[0])

        jsn_dict['ID'] = str(i)
        jsn_dict['Observe'] = str(obsList)
        jsn_dict['Evaluate'] = str(evaList)
        jsn_dict['Predict'] = str(preList)

        json.dumps(jsn_dict, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=True)
        print (jsn_dict)
        jsn_Dict['Data'].append(jsn_dict)
        jsn_Dict = deepcopy(jsn_Dict)
        print (jsn_Dict)

with open("result.json", "w") as f:
    json.dump(jsn_Dict, f)
f.close()