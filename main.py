import pandas as pd
import time
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers, Input
from RubiksCube import Cube
from scramblesearch import ScrambleSearch

# The environment
rc = Cube()
# Instance for ScrambleSearch class for functions (e.g. formatInputs)
ss_ = ScrambleSearch("", 1)

# Make the Neural Network
def buildModel():
  inputs = keras.Input(shape=(48,))
  x = layers.Flatten()(inputs)
  # x = layers.Conv1D(2, 1, activation="relu", input_shape = (48,))(x)
  x = layers.Dense(128, activation="relu")(x)
  x = layers.Dense(128, activation="relu")(x)
  x = layers.Dense(128, activation="relu")(x)
  outputs = layers.Dense(18, activation="sigmoid")(x)
  model = keras.Model(inputs, outputs)
  # Compile the model
  model.compile(optimizer="adam", loss='mean_squared_error')
  return model

def modelSearch(scrambles: int, searches: int, policy, saveid: int, trackprog: bool=False, loadpath: str=None) -> dict:
  if loadpath is None:
    train_data = {"scrambles":[], "moves":[], "evals":[]}
  else:
    tdf = pd.read_csv(loadpath)
    train_data = {"scrambles":list(tdf.scrambles), "moves":list(tdf.moves), "evals":list(tdf.evals)}
  for s in range(scrambles):
    scr = rc.scramble(20)
    print(f"Scramble: {scr}")
    ss = ScrambleSearch(scr, searches)
    t0 = time.time()
    new_train_data = ss.search(policy, 20, trackprog, round(min(searches / 10, 100)))
    dt = round(time.time() - t0)
    print(f"Time elapsed for {searches} searches = {dt//60}:{dt - 60 * (dt // 60)}")
    for t in train_data:
      if len(train_data[t]) == 0:
        train_data[t] = new_train_data[t]
      else:
        for x in new_train_data[t]:
          train_data[t].append(x)
    # Save the training data
    tdf = pd.DataFrame(train_data)
    tdf = tdf.drop_duplicates().reset_index(drop="index")
    tdf.to_csv(f"traindata {saveid} {s+1}-{scrambles}.csv", index=False)
  return train_data

def trainModel(scrambles: int, searches: int, loops: int, policy, trainprop: float = 1, loadpath:str = None, 
                trainlim: int= 64, batch_size: int=64, epochs: int=8, trackprog: bool=False):
  for a in range(loops):
    if a > 0:
      loadpath = None
    train_data = modelSearch(scrambles, searches, policy, a+1, trackprog, loadpath)
    traindf = pd.DataFrame(train_data)
    traindf = traindf.drop_duplicates()
    l = len(traindf.evals)
    print(f"Training data length = {l}")
    print(f"Training data mean score = {round(np.mean(traindf.evals), 2)}")
    traindf = traindf.sort_values("evals", ascending=False).reset_index(drop="index")
    # Create the training data
    x_train = []
    y_train = []
    scrambles_ = list(traindf.scrambles.unique())
    scrambledicts = {s: rc.move_sim(s) for s in scrambles_}
    if trainprop * l < 1:
      trainnum = l
    else:
      trainnum = round(trainprop * l)
    for i in range(min(trainnum, trainlim)):
      scr = traindf.scrambles[i]
      scrdict = scrambledicts[scr]
      trainmoves = rc.qtm(traindf.moves[i])
      seq = ""
      for tm in trainmoves:
        xinput = ss_.formatInputs(rc.move_sim(seq, scrdict))
        seq += tm
        yinput = []
        for j, m in enumerate(ss_.validmoves):
          if m == tm:
            yinput.append(1)
          else:
            yinput.append(0)
        x_train.append(xinput)
        y_train.append(yinput)
    # Train the policy network
    policy.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)
    # Saves trained model for the cycle
    policy.save(f"fmcskel{a}.h5")
    
   if __name__ == "__main__":
    policy = buildModel()
    # Speed ~ 2,560 searches / hour
    trainModel(16, 512, 5, policy)
