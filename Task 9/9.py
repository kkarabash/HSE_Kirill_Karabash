import time
from random import randint
import hashlib
from collections import deque, Counter
import numpy as np

d1_array = np.array([1, 2, 3, 4])
d2_array = np.array([[1, 2, 3, 4],
                     [1, 2, 3, 4],
                     [1, 2, 3, 4],
                     [1, 2, 3, 4]])
d3_array = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                     [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                     [[1, 2, 3], [1, 2, 3], [1, 2, 3]]])

list_array = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
              [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
              [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]

stack = list()
queue = deque()
print("stop")