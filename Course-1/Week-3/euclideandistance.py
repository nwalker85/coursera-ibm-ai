from scipy.spatial import distance
a = (54, 190, 3)
b = (50, 200, 8)
dst = distance.euclidean(a, b)
print(dst)