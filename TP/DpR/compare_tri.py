from tri_fusion import tri_fusion
from tri_insert import tri_insertion
from time import process_time
from random import shuffle

def compare(f1, f2):
    """
    Compare the time between two sorting functions
    """
    result = []
    for i in range(1000, 5000, 100):
        elm = [e for e in range(i)]
        shuffle(elm)

        time1_start = process_time()*1000
        f1(elm)
        time1_end = process_time()*1000

        time2_start = process_time()*1000
        f2(elm)
        time2_end = process_time()*1000

        time1 = time1_end - time1_start
        time2 = time2_end - time2_start

        result.append([i, time1, time2])
    return result

compare(tri_insertion, tri_fusion)


         
