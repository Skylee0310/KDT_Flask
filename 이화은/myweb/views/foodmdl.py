import joblib
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import cv2
import os
from torchvision.transforms.functional import to_pil_image

class CNN(nn.Module) :
    def __init__(self) : # 모델의 구조를 정의 후, 초기화
        super().__init__() # 부모 클래스인 nn.Module의 초기화 메서드를 호출
        self.conLayer = nn.Conv2d(in_channels=3, out_channels=25, kernel_size = 3) # 합성곱 레이어1 정의
        self.conLayer2 = nn.Conv2d(in_channels=25, out_channels=16, kernel_size = 3) # 합성곱 레이어2 정의
        self.conLayer3 = nn.Conv2d(in_channels=16, out_channels=10, kernel_size = 3) # 합성곱 레이어3 정의
        
        self.pool = nn.MaxPool2d(2, 2) 
        self.fc1 = nn.Linear(360, 180)
        self.fc2 = nn.Linear(180, 2)

    def forward(self, x) :
        
        x = self.conLayer(x)
        x = F.relu(x)
        x = self.pool(x)
        
        x = self.conLayer2(x)
        x = F.relu(x)
        x = self.pool(x)

        x = self.conLayer3(x)
        x = F.relu(x)
        x = self.pool(x)
        
        x = x.view(-1, 360)
        
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)

        return x
    
def mymdl():
    model_name = '/model.pth'
    # model_path = 'myweb/views/model.pth'
    pklfile = os.path.dirname(__file__) + model_name
    mdl = torch.load(pklfile)
    return mdl

def img_predict(pic_path, mdl) :
    # 이미지 전처리 시 사용
    preprocessing = transforms.Compose(
        [transforms.Resize(size=(64, 64)), # 사이즈 조정 64 * 64
        transforms.ToTensor()]# 텐서로 변환
    )

    testPic = cv2.imread(pic_path)
    test_pil = to_pil_image(testPic)

    if os.path.exists(pic_path) :
        transformed_img = preprocessing(test_pil)
        transformed_img = transformed_img.unsqueeze(0) # 배치 차원을 추가
        
        mdl.eval()
        with torch.no_grad() : # 그래디언트 업데이트 X
            output = mdl(transformed_img) # 전처리된 이미지를 모델에 입력하여 출력을 계산
            _, predicted = torch.max(torch.softmax(output, dim=1).data, 1) # 모델의 출력에 소프트맥스 함수를 적용하여 확률값으로 변환
            result = f"{100*torch.softmax(output, dim=1).data[0][predicted].item():.1f}% 확률로 {'음식물 쓰레기로 분리배출 가능합니다' if predicted.item() else '음식물 쓰레기로 분리배출 할 수 없습니다'}!"
        return result
