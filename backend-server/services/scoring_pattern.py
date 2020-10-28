import nltk


def return_bleu_score():
    hypothesis = ["open", "the", "file"]
    reference = ["open", "file"]
    # the maximum is bigram, so assign the weight into 2 half.
    BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis, weights=(0.5, 0.5))
    print(BLEUscore)


if __name__ == '__main__':
    return_bleu_score()
