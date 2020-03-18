#!/bin/bash

echo "Εἶπεν δὲ παραβολὴν πρὸς αὐτοὺς λέγων Ἀνθρώπου τινὸς πλουσίου εὐφόρησεν ἡ χώρα." | \
  python -m apply_bpe -c Perseus/bpe.codes --vocabulary Perseus/bpe.vocab.en \
                                   --vocabulary-threshold 50 | \
  python -m sockeye.translate -m March18Model 2>/dev/null | \
  sed -r 's/@@( |$)//g'