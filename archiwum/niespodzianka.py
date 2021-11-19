import imageio
from pathlib import Path
from wordcloud import WordCloud

mask_image=imageio.imread('mask_choinka.png')
text = Path(r'requirements.txt').read_text()

wordcloud = WordCloud(width=1000,height=1000,colormap='prism',mask=mask_image,background_color='white')

wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file('Christmas.png')
