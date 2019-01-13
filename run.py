__author__ = "Jakob Aungiers"
__copyright__ = "Jakob Aungiers 2018"
__version__ = "2.0.0"
__license__ = "MIT"

import os
import json
import time
import math
import matplotlib.pyplot as plt
from core.data_processor import DataLoader
from core.model import Model
import numpy as np

def plot_results(predicted_data, true_data):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.show()


def plot_results_multiple(predicted_data, true_data, prediction_len):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
	# Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
        plt.legend()
    plt.show()


def main():
    configs = json.load(open('config.json', 'r'))
    if not os.path.exists(configs['model']['save_dir']): os.makedirs(configs['model']['save_dir'])
    
    rate=configs['data']['columns'][0]=="Return"

    data = DataLoader(
        os.path.join('data', configs['data']['filename']),
        configs['data']['train_test_split'],
        configs['data']['columns'],
        rate
    )

    model = Model()
    model.build_model(configs)
    x, y = data.get_train_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise']
    )
    
    from keras.utils import plot_model
    plot_model(model.model, to_file='model.png')

#################### Training Section
    in_memory_training=True

    if (in_memory_training):
	# in-memory training
	    model.train(
		    x,
		    y,
		    epochs = configs['training']['epochs'],
		    batch_size = configs['training']['batch_size'],
		    save_dir = configs['model']['save_dir']
	    )
    else:
        # out-of memory generative training
        steps_per_epoch = math.ceil((data.len_train - configs['data']['sequence_length']) / configs['training']['batch_size'])
        model.train_generator(
            data_gen=data.generate_train_batch(
                seq_len=configs['data']['sequence_length'],
                batch_size=configs['training']['batch_size'],
                normalise=configs['data']['normalise']
            ),
            epochs=configs['training']['epochs'],
            batch_size=configs['training']['batch_size'],
            steps_per_epoch=steps_per_epoch,
            save_dir=configs['model']['save_dir']
        )

#################### Test Section
    x_test, y_test = data.get_test_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise']
    )

#################### Multiple Prediction Section

    #predictions = model.predict_sequences_multiple(x_test, configs['data']['sequence_length'], configs['data']['sequence_length'])
    predictions = model.predict_sequence_full(x_test, configs['data']['sequence_length'])
    #predictions = model.predict_point_by_point(x_test)


    if rate:
        np.savetxt('rate_y_test.csv', y_test, delimiter=',')    
        np.savetxt('rate_predictions.csv', predictions, delimiter=',')   # X is an array
    else:
        data.save_test_data('test.csv')
        np.savetxt('y_test.csv', y_test, delimiter=',')
        np.savetxt('predictions.csv', predictions, delimiter=',')   # X is an array
    
    #plot_results_multiple(predictions, y_test, configs['data']['sequence_length'])
    #plot_results(predictions, y_test)

if __name__ == '__main__':
    main()