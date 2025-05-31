#%%
import numpy as np
import matplotlib.pyplot as plt
import wordcloud
#%%
import wordcloud
text = '파이썬 Matplotlib 공부하기'
wc = wordcloud.WordCloud(font_path='C:\\Windows\\Fonts\\HMKMMAG.TTF')
wc.generate_from_text(text)
wc.to_image()
# %%
plt.savefig('Ripple image', dpi=300, bbox_inches='tight')
