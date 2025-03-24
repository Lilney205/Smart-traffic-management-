import cv2
import numpy as np

# Load YOLO model
net = cv2.dnn.readNet("model/yolov4.weights", "model/yolov4.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load class labels
with open("model/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load image
image = cv2.imread("traffic.jpg")
height, width, channels = image.shape

# Preprocess image for YOLO
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
detections = net.forward(output_layers)

# Process detections
car_count = 0
for detection in detections:
    for obj in detection:
        scores = obj[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        # Detect only cars (class_id = 2 in COCO dataset)
        if classes[class_id] == "car" and confidence > 0.5:
            car_count += 1
            center_x, center_y, w, h = (obj[0:4] * np.array([width, height, width, height])).astype("int")
            x, y = int(center_x - w / 2), int(center_y - h / 2)

            # Draw bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, f"Car: {int(confidence * 100)}%", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display results
cv2.imshow("YOLO Car Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Total Cars Detected: {car_count}")
