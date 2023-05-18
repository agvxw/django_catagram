import torch

def yolodetect(image):
    name =[]
    myfile = open("catagram/yolo/name.txt", "r")
    for i in myfile:
        line = str(i)
        line = line.strip('\n')
        name.append(line)
# โหลดโมเดล YOLOv7
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


# ทำการตรวจจับวัตถุและวาดกรอบสี่เหลี่ยมรอบวัตถุที่ตรวจพบบนภาพ
    results = model(image)
    for detection in results.xyxy[0]:
        label = name[int(detection[5])]
        if label == 'cat':
            return label



# แสดงผลภาพ

