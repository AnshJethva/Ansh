import numpy as np

temp = np.array([1,3,40,5,6,3,2])

# mean
print(np.mean(temp))

# meadin
print(np.median(temp))

#standard deviation
print(np.std(temp))

arr = np.array([19,33,66,32,np.nan,76,44,np.nan])
print(np.nanmean(arr))
print(np.nanmean(arr))
print(np.nanstd(arr))