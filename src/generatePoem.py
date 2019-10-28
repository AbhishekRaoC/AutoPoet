import pandas as pd 
import markovify

dataIn= pd.read_csv('../src/poemDataset.csv')

dataIn.head(1)

text_model = markovify.NewlineText(dataIn, state_size=2)

for i in range(5):
    print(text_model.make_sentence())