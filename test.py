import numpy as np
import matplotlib.pyplot as plt

M, N = 5, 8

x = np.linspace(0,2,M+1)
y = np.linspace(0,1,N+1)
X,Y = np.meshgrid(x,y)

positions = np.vstack([Y, X])

is_perimeter = (positions[0] == np.min(y)) | (positions[0] == np.max(y)) | \
               (positions[1] == np.min(x)) | (positions[1] == np.max(x))

print(positions.shape)