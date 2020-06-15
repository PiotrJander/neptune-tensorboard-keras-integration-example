import random
import neptune
from tensorflow import keras
import neptune_tensorboard as neptune_tb

# set project and start integration with keras
neptune.init()
neptune_tb.integrate_with_keras()

# parameters
PARAMS = {'epoch_nr': 5,
          'batch_size': 256,
          'lr': 0.005,
          'momentum': 0.4,
          'use_nesterov': True,
          'unit_nr': 256,
          'dropout': 0.05}

# start experiment
e = neptune.create_experiment(name='keras-integration-example', params=PARAMS)

mnist = keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = keras.models.Sequential([
  keras.layers.Flatten(),
  keras.layers.Dense(PARAMS['unit_nr'], activation=keras.activations.relu),
  keras.layers.Dropout(PARAMS['dropout']),
  keras.layers.Dense(10, activation=keras.activations.softmax)
])

optimizer = keras.optimizers.SGD(lr=PARAMS['lr'],
                                 momentum=PARAMS['momentum'],
                                 nesterov=PARAMS['use_nesterov'],)

model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=PARAMS['epoch_nr'],
          batch_size=PARAMS['batch_size'])

