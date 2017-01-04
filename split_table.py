#!/usr/bin/env python

import pandas
import os

def get_V_pattern(filename, pattern='IGHV11-2*'):
    """
    return indices for sequences containing a specific VH pattern
    """
    full_table = pandas.read_table(filename, index_col=0)
    productive_table = full_table[full_table.Functionality == 'productive']
    matched_index = productive_table[productive_table['V-GENE and allele'].str.contains(pattern)].index
    other_index = productive_table.index.difference(matched_index)
    
    return matched_index, other_index
    
def get_N_indices(filename):
    """
    return indices for sequences containing any N1 or N2 regions, vs. those containing neither
    """
    full_table = pandas.read_table(filename, index_col=0)
    productive_table = full_table[(full_table.Functionality == 'productive') & (full_table['D-REGION-nt nb'] > 0)]
    matched_index = productive_table[(productive_table['N1-REGION-nt nb'] > 0) | (productive_table['N2-REGION-nt nb'] > 0)].index
    other_index = productive_table.index.difference(matched_index)
    
    return matched_index, other_index

def create_subsets(input_filename, output_filename, index_subset):
    """
    Create a new file, containing only specified indices.
    Re-index the new table before writing.
    """
    
    full_table = pandas.read_table(input_filename, index_col=0)
    subset_table = full_table.ix[index_subset]
    subset_table.index = range(1, len(index_subset)+1)
    subset_table.to_csv(output_filename, sep="\t", index_label="Sequence number")

def main_V_pattern(filenames, output_matched, output_other, pattern, n_region=False):
    # get indices from file 6_...
    matched_index = None
    other_index = None
    for filename in filenames:
        if '6_Junction' in filename:
            if n_region:
                matched_index, other_index = get_N_indices(filename)
            else:
                matched_index, other_index = get_V_pattern(filename, pattern)
            break
    
    # find/create output directories
    if not os.path.exists(output_matched):
        os.makedirs(output_matched)
    if not os.path.exists(output_other):
        os.makedirs(output_other)
    
    # iterate through files and write output
    for filename in filenames:
        if '11_Parameters' in filename or 'README' in filename:
            continue
        
        for index, output_directory in zip((matched_index, other_index), (output_matched, output_other)):
            output_filename = os.path.join(output_directory, os.path.basename(filename))
            create_subsets(filename, output_filename, index)

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('textfiles', help="List of output files from IMGT", nargs='+')
    parser.add_argument('out1', help="Directory for IGVH11-2 results.")
    parser.add_argument('out2', help="Directory for other results")
    parser.add_argument('pattern', help="V pattern, e.g. 'IGHV11-2*'")
    parser.add_argument('-n', help="separate based on presence of N regions", action="store_true")
    args = parser.parse_args()
        
    main_V_pattern(args.textfiles, args.out1, args.out2, args.pattern, args.n)