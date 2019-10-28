import pandas as pd 
import markovify

dataIn= pd.read_csv('../src/poemDataset.csv')

text_model = markovify.NewlineText(dataIn.Content, state_size=2)

for i in range(5):
    print(text_model.make_sentence())