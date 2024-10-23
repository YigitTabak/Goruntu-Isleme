import numpy as np
import cv2

image_path = 'images/image.jpg'  

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

c = 20

log_transformed_image = c * np.log1p(image)  

log_transformed_image = np.clip(log_transformed_image, 0, 255).astype(np.uint8)

print("Orijinal Görüntü Boyutları:", image.shape)
print("Logaritma Dönüştürülmüş Görüntü Boyutları:", log_transformed_image.shape)

cv2.imwrite('images/log_transformed_image.jpg', log_transformed_image)

cv2.imshow("Logaritma Dönüşümü", log_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
