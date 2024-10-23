import numpy as np
import cv2

image_path = 'images/image.jpg'  


image = cv2.imread(image_path)

negative_image = 255 - image  

negative_array = negative_image.astype(np.uint8)


print("Orijinal Görüntü Boyutları:", image.shape)
print("Negatif Görüntü Boyutları:", negative_array.shape)

cv2.imwrite('images/negative_image.jpg', negative_array)

cv2.imshow("Negatif Görüntü", negative_array)
cv2.waitKey(0)
cv2.destroyAllWindows()
