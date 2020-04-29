from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["2\nBorg win\nMcEnroe loss","[\u0027Borg\u0027]\n1"],["3\nMcEnroe win\nBorg loss\nMcEnroe win","[\u0027McEnroe\u0027, \u0027McEnroe\u0027]\n2"]])