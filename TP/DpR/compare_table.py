from compare_tri import compare
from tri_fusion import tri_fusion
from tri_insert import tri_insertion
from prettytable import PrettyTable

def compare_table(f1, f2):
    """
    Compare the time between two sorting functions in table
    """
    x = PrettyTable()
    x.field_names = ["Elements", "Functions 1 (ms)", "Function 2 (ms)"]

    x.add_rows(compare(f1,f2))
    return x

print(compare_table(tri_insertion, tri_fusion))
