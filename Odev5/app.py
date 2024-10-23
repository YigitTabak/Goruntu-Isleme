import numpy as np
import cv2


image_path = 'images/image.jpg' 


image = cv2.imread(image_path)
if image is None:
    raise ValueError("Görüntü yüklenemedi. Dosya yolunu kontrol edin.")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


c = 1  
gamma = 1.5  


height, width = image_gray.shape
result_image = np.zeros_like(image_gray, dtype=np.float64)


for i in range(height):
    for j in range(width):
        r = image_gray[i, j] / 255.0  
        S = c * (r ** gamma)  
        result_image[i, j] = S


result_image = (result_image * 255).astype(np.uint8)


result_image = np.clip(result_image, 0, 255)  


cv2.imwrite('images/power_law_transformed_image.jpg', result_image)
cv2.imshow("Kuvvet Kanunu Dönüşümü", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
