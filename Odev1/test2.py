import cv2
import numpy as np

def detect_underfilled_bottles(image_path, height_threshold):
    image = cv2.imread(image_path)
    
    if image is None:
        print("Resim yüklenemedi. Dosya yolunu kontrol et.")
        return
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        if h < height_threshold:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    cv2.imwrite('detected_bottles.png', image)
    print("İşlenmiş resim 'detected_bottles.png' olarak kaydedildi.")

detect_underfilled_bottles('C:\\Users\\Yigit\\Desktop\\sise.png', 150)
