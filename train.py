import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# load data
data = pd.read_csv('dataset/dataset.csv',index_col=False) 
data.fillna(0,inplace=True)
data = data.reset_index(drop=True)

X = data.iloc[:,:-1].astype(int).values # همه ردیف ها تا ستون اخر
Y = data.iloc[: ,-1].astype(int).values # همه ردیف ها فقط ستون اخرشون



X_train , X_test ,Y_train ,Y_test = train_test_split(X,Y, test_size=0.2, shuffle=True)


model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(14 , activation='sigmoid') , 
    tf.keras.layers.Dense(30,activation='relu') , 
    tf.keras.layers.Dense(16,activation='relu') , 
    tf.keras.layers.Dense(4 , activation='softmax')
])

Y_train= Y_train.reshape(-1,1) 

Y_test= Y_test.reshape(-1,1)

model.compile(optimizer='adam' ,
              loss='sparse_categorical_crossentropy' , 
              metrics=['accuracy']
)

output = model.fit(X_train,Y_train,epochs=10)

loss , accuracy = model.evaluate(X_test,Y_test)

model.save('weights/snake_game_model.h5')

