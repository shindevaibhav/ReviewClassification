import text_input
import re
import pandas as pd
import train
import model
import numpy as np
import os
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
train_dir = './train'

class Prediction(object):
    def __init__(self, suffix='Summary'):
        self.reader = text_input.TextReader('./data/mr/', suffix=suffix)
        self.reader.prepare_data(vocab_size=4000, test_fraction=0.1)
        if(os.path.exists(train_dir+"_"+suffix)):
            with tf.Graph().as_default():
                with tf.variable_scope('cnn'):
                    self.model = model.Model(FLAGS, is_train=False)
                saver = tf.train.Saver(tf.all_variables())

                self.sess = tf.Session()
                ckpt = tf.train.get_checkpoint_state("train_"+suffix+"/")
                #print ckpt
                #print ckpt.model_checkpoint_path
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(self.sess, ckpt.model_checkpoint_path)
                else:
                    raise IOError("Loading checkpoint file failed!")
        else:
            train.train(suffix)
            self.sess = train.sess
            self.model = train.m
    def get_prediction(self,string):
        #string = "Overall I felt that the student made a good effort to explain their ideas.  1. An unspecified rough app or computer program.  2. A series of sensors in bikes and/ or cars that alert drivers/ cyclists to potential collisions.  3. An app that the city/ police can use to see where cyclist have had accidents or poor experiences so that changes can be made to prevent future accidents."
        clean_string = self.reader.clean_str(string)
        toks = clean_string.split()
        toks_len = len(toks)
        max_sent_len = self.reader.max_sent_len
        if toks_len <= max_sent_len:
            pad_left = (max_sent_len - toks_len) / 2
            pad_right = int(np.ceil((max_sent_len - toks_len) / 2.0))
        else:
            pad_left = 0
            pad_right = 0
            toks = toks[:len(max_sent_len)]
        toks_ids = [1 for i in range(pad_left)] + [self.reader.word2id[t] if t in self.reader.word2id else 0 for t in toks] + [1 for i in range(pad_right)]
        x = []
        x.append(toks_ids)

        x = np.array(x)
        logits = self.sess.run([self.model.logits], feed_dict={self.model.inputs: x})
        print logits
        if logits[0][0][0] > logits[0][0][1]:
            return "positive"
        else:
            return "negative"

def main():
    pred = Prediction(suffix='Summary')
    df_summary_pos = pd.read_csv("csv/_summary_pos.csv")
    string = df_summary_pos.iloc[35]["Comments"]
    print string
    print pred.get_prediction(string)
    df_summary_neg = pd.read_csv("csv/_summary_neg.csv")
    string = df_summary_neg.iloc[3]["Comments"]
    print string
    print pred.get_prediction(string)


if __name__ == '__main__':
    main()

'''
y_batch = list(data_loader._y[50:99]) + [0]
loss_value, true_count_value = sess.run([mtest.total_loss, mtest.true_count_op], 
                    feed_dict={mtest.inputs: x_batch, mtest.labels: y_batch})
print data_loader._y[0:49]

df_praise_pos = pd.read_csv("csv/_praise_pos.csv")
len(df_praise_pos)
df_praise_neg = pd.read_csv("csv/_praise_neg.csv")
len(df_praise_neg)

df_mitigation_pos = pd.read_csv("csv/_mitigation_pos.csv")
len(df_mitigation_pos)
df_mitigation_neg = pd.read_csv("csv/_mitigation_neg.csv")
len(df_mitigation_neg)

df_localization_pos = pd.read_csv("csv/_localization_pos.csv")
len(df_localization_pos)
df_localization_neg = pd.read_csv("csv/_localization_neg.csv")
len(df_localization_neg)


df_neutrality_pos = pd.read_csv("csv/_neutrality_pos.csv")
len(df_neutrality_pos)
df_neutrality_neg = pd.read_csv("csv/_neutrality_neg.csv")
len(df_neutrality_neg)

df_problem_pos = pd.read_csv("csv/_problem_pos.csv")
len(df_problem_pos)
df_problem_neg = pd.read_csv("csv/_problem_neg.csv")
len(df_problem_neg)

df_solution_pos = pd.read_csv("csv/_solution_pos.csv")
len(df_solution_pos)
df_solution_neg = pd.read_csv("csv/_solution_neg.csv")
len(df_solution_neg)

df_summary_pos = pd.read_csv("csv/_summary_pos.csv")
len(df_summary_pos)
df_summary_neg = pd.read_csv("csv/_summary_neg.csv")
len(df_summary_neg)
'''
