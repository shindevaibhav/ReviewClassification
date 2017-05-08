A Tensorflow implementation of convolutional neural network to classify sentences
=========
This implementation uses Tensorflow's `tf.conv2d` to perform 1D convolution on word sequences. It also supports using Google News word2vec pre-trained vectors to initialize word embeddings, which boosts the performance on movie review dataset from ~76% to ~81%.

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

#### Start the service
    python service.py

    
    
## References

1. Kim, Yoon. "Convolutional neural networks for sentence classification." arXiv preprint arXiv:1408.5882 (2014). [link](http://arxiv.org/abs/1408.5882)

## License
MIT
