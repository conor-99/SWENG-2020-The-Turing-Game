# Class worked on by: Leo
# -*- coding: utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import tensorlayer as tl
import numpy as np
from data_pre_processor import DataPreProcessor
from data.twitter import data
from tensorlayer.cost import cross_entropy_seq, cross_entropy_seq_with_mask
from tqdm import tqdm
from sklearn.utils import shuffle
from tensorlayer.models.seq2seq import Seq2seq
from tensorlayer.models.seq2seq_with_attention import Seq2seqLuongAttention

# The following code is adapted (mostly) from https://github.com/tensorlayer/seq2seq-chatbot
class AI:
    input = ""
    model_ = 0

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
    def __init__(self, name):
        self.name = name
        self.preProcessor = DataPreProcessor(userInput)
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

    # Handle the creation of a response from the given input
    def respond(self, seed, number):
        sentence = self.simpleResponse(seed)

        self.model_.eval()
        seed_id = [self.word2idx.get(w, self.unk_id) for w in seed.split(" ")]
        sentence_id = self.model_(inputs=[[seed_id]], seq_length=20, start_token=self.start_id, top_n=number)
        for w_id in sentence_id[0]:
            w = self.idx2word[w_id]
            if w == 'end_id':
                break
            sentence = sentence + [w]

        if sentence == []:
            sentence = ["I'm", "sorry,", "I", "just", "don't", "quite", "understand", "what", "you're", "asking..."]
        return sentence

    def simpleResponse(self, input):
        sentence = []
        input = self.preProcessor.string2Array(seed)
        tally = [0, 0, 0]
        greetings = ["hello","hi","greetings","hey"]

        for x in input:
            x = 0
        return sentence
