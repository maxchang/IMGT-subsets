#!/usr/bin/env python

import pandas
import os

CDR3_SEQUENCE_COLUMN = 20


def CDR3_from_summary(filename):
    CDR3_df = pandas.read_table(filename, usecols=[CDR3_SEQUENCE_COLUMN])
    CDR3_count = CDR3_df.ix[:,0].value_counts()
    CDR3_count.name = 'Occurrences'

    # write to the same directory as the input file
    input_directory = os.path.split(os.path.abspath(filename))[0]
    output_filename = os.path.join(input_directory, 'CDR3_count.csv')
    CDR3_count.to_csv(output_filename, header=True, index_label='CDR3')

if __name__ == '__main__':
    import sys

    for filename in sys.argv[1:]:
        CDR3_from_summary(filename)

