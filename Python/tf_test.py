#Neural Network to Classify Images
#Handwritten Digits

import tensorflow as tf

#Load & Prepare the MNIST Datasets
mnist = tf.keras.datasets.mnist

#Convert the samples from int to float
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.

#Build the model by stacking layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

#Model returns "Logits" or "Log-Odds"
predictions = model(x_train[:1]).numpy()
predictions

#Function converts these Logits to "Probabilities"
tf.nn.softmax(predictions).numpy()

#Vector of logits + True index and returns a scalar loss
    #Loss equal to the neg. log prob. of the true class
    #It is zero if the model is sure of the correct class
    #This untrained model gives prob close to rdm (1/10 for each class)
    #so the initial loss should be close to -tf.log(1/10) ~= 2.3
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

model.compile(
    optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy']
)

#"Model.fit" method adjusts the model param to mimize the loss
model.fit(x_train, y_train, epochs=5)

#'Model.evaluate' checks the models performance on a test
model.evaluate(x_test, y_test, verbose=2)

#Return a probability, wrap the trained model, and attach the softmax to it
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

probability_model(x_test[:5])
