#%%

import numpy as np
# %%
l = [1, 2, 3, 4]


# %%
print(l*3)
# %%
for i in range(len(l)):
    l[i]  = l[i] *3
print(l)
# %%
l = [1, 2, 3, 4]
a = np.array(l)
# %%
print(a[0])
# %%
