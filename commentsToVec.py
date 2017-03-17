import pandas as pd
import re
import os
from gensim.models.doc2vec import LabeledSentence, Doc2Vec
import random

df = pd.read_csv("all_comments.csv")
df.columns.values
headers = list(df.columns.values)
headers.remove("Comments")
df = df.drop(headers,axis=1)
df.head()

comments = []
for index, row in df.iterrows():
    line = row["Comments"]
    line = re.sub("[^a-zA-Z?!]"," ", line)
    words = [w.lower().decode('utf-8') for w in line.strip().split() if len(w)>=3]
    comments.append(words)
i = 0
labeled_comments = []
for comment in comments:
    #print comment
    sentence = LabeledSentence(words=comment, tags=["COMMENT_"+str(i)])
    labeled_comments.append(sentence)
    i += 1
    
#more dimensions mean more trainig them, but more generalized
num_features = 300
# Minimum word count threshold.
min_word_count = 1
# Number of threads to run in parallel.
num_workers = multiprocessing.cpu_count()
# Context window length.
context_size = 10
# Downsample setting for frequent words.
#rate 0 and 1e-5 
#how often to use
downsampling = 1e-4

# Initialize model
model = Doc2Vec(min_count=min_word_count,
	window=context_size, 
	size=num_features,
	sample=downsampling,
	negative=5,
	workers=num_workers)
	
model.build_vocab(labeled_comments)

# Train the model
# This may take a bit to run #20 is better
for epoch in range(10):
    print "Training iteration %d" % (epoch)
    random.shuffle(labeled_comments)
    model.train(labeled_comments)
#save model
if not os.path.exists("trained"):
    os.makedirs("trained")
model.save(os.path.join("trained", "comments2vec.d2v"))
#load model
model = Doc2Vec.load(os.path.join("trained", "comments2vec.d2v"))
