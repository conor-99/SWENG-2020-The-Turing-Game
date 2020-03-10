# Class worked on by: Claire, Luiz Fellipe, Leo
# -*- coding: utf-8 -*-
'''
import tensorflow as tf
import tensorlayer as tl
import numpy as np
from tensorlayer.cost import cross_entropy_seq, cross_entropy_seq_with_mask
from tqdm import tqdm
from sklearn.utils import shuffle
from tensorlayer.models.seq2seq import Seq2seq
from tensorlayer.models.seq2seq_with_attention import Seq2seqLuongAttention
import os
'''
from data_pre_processor import DataPreProcessor
from teenager import Teenager
from young_adult import YoungAdult
from adult import Adult
from data_post_processor import DataPostProcessor
import random

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # Where input is user input from commandline.
    print('\033[1m' + "Enter the input, or enter 'exit' to end:" + '\033[0m')

    personality = None

    # Personality is randomly assigned between teenager, young adult and adult with a random name each time.
    perNum = random.randint(1, 3)
    if perNum == 1:
        personality = Teenager("Jane Doe")
    elif perNum == 2:
        personality = YoungAdult("James Doe")
    else:
        personality = Adult("Janet Doe")

    while(1):
        userInput = input()

        # exit on 'exit'.
        if(userInput == "exit"):
            break

        output = arrangeResp(userInput, personality)

        print('\033[94m' + "--> " + str(output) + '\033[0m')
        print('\033[1m' + "Enter another input:" + '\033[0m')
    print('\033[92m' + "Program exited." + '\033[0m')

def arrangeResp(userInput, personality):
    # Where output is the processed output.
    preProcessor = DataPreProcessor(userInput)
    preProcessor.processInput()

    # This is passed to the model.
    processedInput = preProcessor.input
    # response = respond(processedInput, 1)
    # postProcessor = DataPostProcessor(response, personality)

    return processedInput

'''
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

    src_vocab_size = tgt_vocab_size = src_vocab_size + 2
    vocabulary_size = src_vocab_size

    decoder_seq_length = 20

    model_ = Seq2seq(
        decoder_seq_length = decoder_seq_length,
        cell_enc=tf.keras.layers.GRUCell,
        cell_dec=tf.keras.layers.GRUCell,
        n_layer=3,
        n_units=256,
        embedding_layer=tl.layers.Embedding(vocabulary_size=vocabulary_size, embedding_size=emb_dim),
        )

    load_weights = tl.files.load_npz(name='model.npz')
    tl.files.assign_weights(load_weights, model_)

    def respond(seed, number):
        model_.eval()
        seed_id = [word2idx.get(w, unk_id) for w in seed.split(" ")]
        sentence_id = model_(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n=number)
        sentence = []
        for w_id in sentence_id[0]:
            w = idx2word[w_id]
            if w == 'end_id':
                break
            sentence = sentence + [w]
        return sentence
'''

if __name__ == '__main__':
    main()
