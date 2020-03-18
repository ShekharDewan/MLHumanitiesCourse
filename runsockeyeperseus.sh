#!/bin/bash

python -m learn_joint_bpe_and_vocab --input ~/MLHumanitiesCourse/SockeyeReady/InputGreek.txt ~/MLHumanitiesCourse/SockeyeReady/OutputEnglish.txt \
                                    -s 30000 \
                                    -o Perseus/bpe.codes \
                                    --write-vocabulary Perseus/bpe.vocab.de Perseus/bpe.vocab.en

python -m apply_bpe -c Perseus/bpe.codes --vocabulary Perseus/bpe.vocab.de --vocabulary-threshold 50 < ~/MLHumanitiesCourse/SockeyeReady/train_source.txt > Perseus/train_source.BPE
python -m apply_bpe -c Perseus/bpe.codes --vocabulary Perseus/bpe.vocab.en --vocabulary-threshold 50 < ~/MLHumanitiesCourse/SockeyeReady/train_target.txt > Perseus/train_target.BPE

python -m apply_bpe -c Perseus/bpe.codes --vocabulary bpe.vocab.de --vocabulary-threshold 50 < ~/MLHumanitiesCourse/SockeyeReady/dev_source.txt > Perseus/dev_source.BPE
python -m apply_bpe -c Perseus/bpe.codes --vocabulary bpe.vocab.en --vocabulary-threshold 50 < ~/MLHumanitiesCourse/SockeyeReady/dev_target.txt > Perseus/dev_target.BPE

python -m sockeye.prepare_data \
                        -s Perseus/train_source.BPE \
                        -t Perseus/train_target.BPE \
                        -o Perseus/train_data

python -m sockeye.train -d Perseus/train_data \
                        -vs Perseus/dev_source.BPE \
                        -vt Perseus/dev_target.BPE \
                        --encoder rnn \
                        --decoder rnn \
                        --num-embed 128 \
                        --rnn-num-hidden 256 \
                        --rnn-attention-type dot \
                        --max-seq-len 60 \
                        --decode-and-evaluate 500 \
                        -o March18Model