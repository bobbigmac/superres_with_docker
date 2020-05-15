import cv2
from cv2 import dnn_superres

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

#TODO: Colour correct, autolevel, convert to png

# Read image
image = cv2.imread('/test/images/frame1.png')
# image = cv2.imread('/test/images/smol3.png')

# Read the desired model
path = "/test/models/model1/EDSR_x2.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 2)

# Upscale the image
result = sr.upsample(image)

# Save the image
cv2.imwrite("/test/images/frame1upscaled.png", result)
#cv2.imwrite("/test/images/art1up2.jpg", result)

#TODO potrace to vector
#TODO maybe useful https://gist.github.com/zph/2494870
#TODO maybe useful https://github.com/unpaper/unpaper
#TODO maybe useful http://www.fmwconcepts.com/imagemagick/textcleaner/index.php