load FSEQ.hdl,
output-file FSEQ2.out,
compare-to FSEQ2.cmp,
output-list E%B3.1.3 F%B3.1.3 G%B3.1.3;


set load 1,
set f1 1,
set f0 1,
set A 0,
set B 1,
set C 0,
set D 1,
tick,
tock;

set load 0,
set f1 0,
set f0 0,
tick,
tock;

output;
