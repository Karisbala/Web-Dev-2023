def combo_string(a, b):
    if len(a) < len(b):
        short = a
        long = b
    else:
        long = a
        short = b
    return short + long + short
