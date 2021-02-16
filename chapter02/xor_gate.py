from chapter02.and_gate import and_gate
from chapter02.nand_gate import nand_gate
from chapter02.or_gate import or_gate


def xor_gate(x1, x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate(s1, s2)
    return y
