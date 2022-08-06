# Display your wordcloud image
from uploader import _upload
from image import calculate_frequencies
import numpy as np
from matplotlib import pyplot as plt
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
