import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from compare_tri import compare
from tri_fusion import tri_fusion
from tri_insert import tri_insertion

def compare_graph3d(f1, f2):
    result = compare(f1, f2)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')