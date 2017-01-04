split_table.py data/PerC_B1a/*txt results/V/PerC_B1a/V11-2 results/V/PerC_B1a/next 'IGHV11-2*'
split_table.py results/V/PerC_B1a/next/*txt results/V/PerC_B1a/V12-3 results/V/PerC_B1a/next2 'IGHV12-3*'
split_table.py results/V/PerC_B1a/next2/*txt results/V/PerC_B1a/V6 results/V/PerC_B1a/other 'IGHV6-'
rm -rf results/V/PerC_B1a/next results/V/PerC_B1a/next2

split_table.py data/spl_B1a/*txt results/V/spl_B1a/V11-2 results/V/spl_B1a/next 'IGHV11-2*'
split_table.py results/V/spl_B1a/next/*txt results/V/spl_B1a/V12-3 results/V/spl_B1a/next2 'IGHV12-3*'
split_table.py results/V/spl_B1a/next2/*txt results/V/spl_B1a/V6 results/V/spl_B1a/other 'IGHV6-'
rm -rf results/V/spl_B1a/next results/V/spl_B1a/next2

src/split_table.py data/PerC_B1b/*txt results/V/PerC_B1b/V11-2 results/V/PerC_B1b/next 'IGHV11-2*'
src/split_table.py results/V/PerC_B1b/next/*txt results/V/PerC_B1b/V12-3 results/V/PerC_B1b/other 'IGHV12-3*'
rm -rf results/V/PerC_B1b/next
