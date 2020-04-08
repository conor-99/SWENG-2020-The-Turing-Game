# Class worked on by: Leo
# -*- coding: utf-8 -*-
import os
# This prevents the incredibly verbose logging that usually accompanies tensorflow from appearing in terminal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
# This should force CPU-only usage
os.environ['CUDA_VISIBLE_DEVICES'] = "-1"

import tensorflow as tf
import tensorlayer as tl
import numpy as np
from random import randint
from data_pre_processor import DataPreProcessor
from data.twitter import data
from tensorlayer.cost import cross_entropy_seq, cross_entropy_seq_with_mask
from tqdm import tqdm
from sklearn.utils import shuffle
from tensorlayer.models.seq2seq import Seq2seq
from tensorlayer.models.seq2seq_with_attention import Seq2seqLuongAttention

# The following code is adapted (mostly) from https://github.com/tensorlayer/seq2seq-chatbot
class AI:
    metadata, idx_q, idx_a = data.load_data(PATH='data/{}/'.format("twitter"))
    src_vocab_size = len(metadata['idx2w'])
    emb_dim = 1024
    word2idx = metadata['w2idx']
    idx2word = metadata['idx2w']
    unk_id = word2idx['unk']
    pad_id = word2idx['_']
    start_id = src_vocab_size
    end_id = src_vocab_size + 1
    word2idx.update({'start_id': start_id})
    word2idx.update({'end_id': end_id})
    idx2word = idx2word + ['start_id', 'end_id']
    src_vocab_size = src_vocab_size + 2
    vocabulary_size = src_vocab_size
    decoder_seq_length = 20

    # Creates an instance of the AI with it's name being passed from a name-generating function
    def __init__(self):
        # preProcessor is only utilised here to avoid duplicating string2array
        self.preProcessor = DataPreProcessor("")
        self.model_ = Seq2seq(
            decoder_seq_length = self.decoder_seq_length,
            cell_enc=tf.keras.layers.GRUCell,
            cell_dec=tf.keras.layers.GRUCell,
            n_layer=3,
            n_units=256,
            embedding_layer=tl.layers.Embedding(vocabulary_size=self.vocabulary_size, embedding_size=self.emb_dim),
            )
        load_weights = tl.files.load_npz(name="data/model.npz")
        tl.files.assign_weights(load_weights, self.model_)

    # Take a name, create a mood
    def initliase(self, name):
        self.name = name
        feelings = ["good","well","great","grand","excellent","ecstatic","happy","sad","annoyed","frustrated","angry","tired","okay","alright"]
        self.feel = feelings[randint(0,len(feelings)-1)]

    # Handle the creation of a response from the given input
    def respond(self, seed, number):
        simpleStart = self.simpleResponse(seed)
        self.model_.eval()
        seed_id = [self.word2idx.get(w, self.unk_id) for w in seed.split(" ")]
        sentence_id = self.model_(inputs=[[seed_id]], seq_length=20, start_token=self.start_id, top_n=number)
        sentence = []
        for w_id in sentence_id[0]:
            w = self.idx2word[w_id]
            if w == 'end_id':
                break
            sentence = sentence + [w]
        # A catch all just in case there are no responses, but we have yet to find an input to trigger this
        if sentence == []:
            sentence = ["I'm", "sorry,", "I", "just", "don't", "quite", "understand", "what", "you're", "asking..."]
        return simpleStart + sentence

    # Handle simple questions that the AI is less than optimal at answering
    def simpleResponse(self, input):
        sentence = []
        input = self.preProcessor.string2Array(input)
        tally = [0, 0, 0]
        greetings = ["hello","hi","greetings","salutations","hey","yo","howdy"]
        names = [["what","who"],["is","are"],["you","your"],["name"]]
        wellbeing = [["how"],["do","are"],["you"],["doing","feeling","feel"]]
        # Tallying key words in the user query to determine if certain questions were being asked
        for x in input:
            for y in range(len(greetings)):
                if x == greetings[y]:
                    tally[0] = 1
                    break
            for y in range(len(names)):
                for z in names[y]:
                    if x is z:
                        tally[1] = tally[1] + 1
                        break
            for y in range(len(wellbeing)):
                for z in wellbeing[y]:
                    if x == z:
                        tally[2] = tally[2] + 1
                        break
        # Handle a return greeting, and maybe ask how the user is
        if tally[0] > 0:
            sentence.append(greetings[randint(0,6)])
            if randint(0,1) is 1:
                sentence.append("how")
                sentence.append("are")
                sentence.append("you")
                value = randint(0,2)
                if value is 0:
                    sentence.append("doing")
                elif value is 1:
                    sentence.append("feeling")
        # Handle questions about it's name with a simple answer
        if tally[1] > 2 and len(input) < 5:
            if randint(0,1) is 1:
                sentence.append("I")
                sentence.append("am")
            else:
                sentence.append("my")
                sentence.append("name")
                sentence.append("is")
            sentence.append(self.name)
        # Handle a 'how are you' type question with a pre-determined emotional state
        if tally[2] > 2 and len(input) < 5:
            sentence.append("I")
            sentence.append("am")
            if randint(0,1) is 1:
                sentence.append("feeling")
            sentence.append(self.feel)
        return sentence
