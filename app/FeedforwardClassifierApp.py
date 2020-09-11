from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from pyqtgraph import ImageView
import camera
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import Models.FeedForward as FeedForward

drawing = False

class StartWindow(QMainWindow):
    def __init__(self, camera = None):
        super().__init__()
        self.camera = camera
        self.central_widget = QWidget()
        self.button_frame = QPushButton('Draw', self.central_widget)
        self.image_view = ImageView()
        self.button_submit = QPushButton('Predict', self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.button_frame)
        self.layout.addWidget(self.image_view)

        self.setCentralWidget(self.central_widget)
        
        self.button_frame.clicked.connect(self.update_image)
        self.button_submit.clicked.connect(self.submit)

    
    def update_image(self):
        #frame = self.camera.get_frame()
        self.frame = canvas()
        self.frame = cv2.cvtColor(self.frame , cv2.COLOR_BGR2GRAY)
        print(self.frame.shape)
        self.image_view.setImage(self.frame.T)

    def submit(self):
        # DEBUG
        #print(self.frame)
        images = torch.from_numpy(self.frame)
        images = images.unsqueeze(0)
        #images = images.unsqueeze(0)
        output = model(images.float()) #.float() because i got error RuntimeError: Expected object of scalar type Float but got scalar type Double for argument #4 'mat1'
        _ , preds = torch.max(output , dim=1)
        print("Prediction: ",preds.item())




def draw_circle(event,x,y,flags,param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            #print('DRAWING!!')
            cv2.circle(img,(x,y),1,(255,255,255),-1)

def canvas():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while(1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    return img

if __name__ == '__main__':
    app = QApplication([])

    # cam = camera.Camera(0)
    # cam.initialize()
    # print(cam)
    img = np.zeros((28, 28, 3), np.uint8)

    model = FeedForward.MNIST_FeedForward()
    trained_params = torch.load('savedModels/MNIST_FeedForward.pth')
    model.load_state_dict(trained_params)
    print("Model Loaded Successfully!!")

    start_window = StartWindow()
    start_window.show()

    app.exit(app.exec_())
