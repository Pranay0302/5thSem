import matplotlib.pylab as plt
from PIL import Image
i = Image.open('../images/a02.jpeg')

imgplot = plt.imshow(i, cmap='gray')
plt.axis("off")
plt.colorbar()
plt.show()
