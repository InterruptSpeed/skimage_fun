#from skimage.data import camera
from skimage.filters import frangi, hessian
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

#image = camera()
image = rgb2gray(imread("lena.png"))
fig, ax = plt.subplots(ncols=3)

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original image')

ax[1].imshow(frangi(image), cmap=plt.cm.gray)
ax[1].set_title('Frangi filter result')

ax[2].imshow(hessian(image), cmap=plt.cm.gray)
ax[2].set_title('Hybrid Hessian filter result')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()