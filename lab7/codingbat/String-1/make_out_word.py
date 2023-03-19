def make_out_word(out, word):
    return "{out1}{word}{out2}".format(out1=out[:2], word=word, out2=out[2:])
