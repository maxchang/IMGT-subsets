#!/usr/bin/env python

import os
import sys
import pandas

SUBSET_POSITION = -3


def merge_CDR3_summaries(filename_list):
    df_list = []
    for filename in filename_list:
        CDR3_df = pandas.read_csv(filename)
        subset_name = os.path.abspath(filename).split(os.sep)[SUBSET_POSITION]
        CDR3_df['subset'] = subset_name
        df_list.append(CDR3_df)
    
    merged_df = pandas.concat(df_list, ignore_index=True)
    merged_wide_df = merged_df.pivot(index="CDR3", columns="subset", values="Occurrences")
    merged_wide_df.fillna(0).to_csv(sys.stdout)
    

if __name__ == '__main__':
    merge_CDR3_summaries(sys.argv[1:])