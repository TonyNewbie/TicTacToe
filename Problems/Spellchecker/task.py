dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input()
incorrect = [word for word in sentence.split() if word not in dictionary]
if len(incorrect) == 0:
    print('OK')
else:
    print('\n'.join(incorrect))
