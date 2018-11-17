from skimage import img_as_uint
from skimage.io import imread, imsave
from skimage.color import rgb2gray, rgb2grey, gray2rgb, rgb2hsv
from skimage.io import imshow, show

# samples originally from: https://seethesource.wordpress.com/2017/02/28/manipulating-image-pixels-with-python-scikit-image-color-schemes/

# read, write
inp_image = imread("lena.png")

# read, write, show
 
#parameter 1: path where the image has to be saved.
#parameter 2: the array of the image.
imsave("new_lena.png",inp_image)

#imshow(inp_image,'matplotlib')
#show()


# the 'matplotlib' is used to tell the viewer to use matplotlib plugin while plotting the image.
 
imsave("lena_new.png",img_as_uint(inp_image)) #img_as_uint is the secret to correctly save images that cannot be saved directly!!

# rgb to gray

img_gray = rgb2gray(inp_image) # rgb2grey(inp_image) can also be used
 
imsave("lena_gray.png",img_gray)

# gray to rgb

inp_img2 = imread("lena_gray.png")
rgb_img = gray2rgb(inp_img2)
imsave("lena_gray2color.png",rgb_img)

# rgb to hsv

hsv_img = rgb2hsv(inp_image)
imsave("lena_hsv.png",hsv_img)

# binarization / thresholding

from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint
 
inp_image = imread("lena.png")
img_gray = rgb2gray(inp_image)
 
thresh = threshold_otsu(img_gray)
binary_thresh_img = img_gray > thresh
 
imsave("lena_thresh.png", img_as_uint(binary_thresh_img))