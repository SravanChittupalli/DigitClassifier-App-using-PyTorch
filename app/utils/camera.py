import cv2 #version 4.2.0.34

class Camera:
    def __init__(self , camera_num):
        self.cam_num = camera_num

    def __str__(self):
        return 'OpenCV camera {}'.format(self.cam_num)
    
    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    def get_frame(self):
        ret , frame = self.cap.read()
        return frame

    def close_camera(self):
        self.cap.release()

    

if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    print(cam)
    ret , frame = cam.get_frame()
    print(frame)
    cam.close_camera()