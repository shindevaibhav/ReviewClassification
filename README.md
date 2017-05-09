A Tensorflow implementation of convolutional neural network to classify sentences
=========

The original theano implementation of this model by the author is [here](https://github.com/yoonkim/CNN_sentence). Another tensorflow implementation that does not support loading pretrained vectors is [here](https://github.com/dennybritz/cnn-text-classification-tf).

## Dependency

- python2.7+
- numpy
- tensorflow 0.7+

## Data

The data in `data/mr/` contains 905 labeled expertiza reviews. The current `data/word2vec` directory is empty. To use the pretrained word2vec embeddings, download the Google News pretrained vector data from
"wget https://s3.amazonaws.com/mordecai-geo/GoogleNews-vectors-negative300.bin.gz"
and unzip it to the directory. It will be a `.bin` file.

## Usage

#### Preprocess the data

    python text_input.py
        This will decide the configuration values for 
            ('vocab_size', 4000, 'Vocabulary size')(model.py)
            ('sent_len', 480, 'max sentence length')(model.py)

#### Start the service
    python service.py --train True  #train = true(will not reuse the earlier saved model)
    ==> http://0.0.0.0:5002/
    
    
## References

1. Kim, Yoon. "Convolutional neural networks for sentence classification." arXiv preprint arXiv:1408.5882 (2014). [link](http://arxiv.org/abs/1408.5882)

## License
MIT
