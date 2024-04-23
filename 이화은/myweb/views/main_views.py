from flask import Blueprint, render_template, request
from flask import current_app
from werkzeug.utils import secure_filename
import os
import PIL
import joblib
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import cv2
import os
from torchvision.transforms.functional import to_pil_image
from .foodmdl import img_predict, CNN
from ..models import FoodWaste
from datetime import datetime
from myweb import db

mdl = CNN()

bp = Blueprint('main',
               __name__,
               template_folder='templates',
               url_prefix = '/')

# 라우팅 함수들
@bp.route('/')
def index() :
    return render_template('input.html')

# 라우팅 함수: 이미지 제출 처리
@bp.route('/classify', methods=['POST'])
def classify():
    try:
        
        file = request.files['img']
        filename = secure_filename(file.filename)

        uploads_dir = os.path.join(current_app.static_folder, 'uploads')
        file_path = os.path.join(uploads_dir, filename)
        print(file_path, filename)

        # Blueprint의 static_folder를 사용하여 파일 저장 경로 생성
        # file_path = os.path.join('static', 'uploads', filename)
        file_path = f'myweb/static/uploads/{filename}'
        file.save(file_path)

        result = img_predict(file_path, mdl)

        col = FoodWaste(type=type, create_date=datetime.now()) # 하나의 행 데이터
        db.session.add(col)     # 행 데이터 추가
        db.session.commit()     # 데이터베이스에 적용. 이걸 해야 server에 적용됨


        # 분류 결과를 result.html에 전달
        return render_template('result.html', filename=filename, result=result)
   
    except Exception as e:

        # 예외 발생 시 오류 메시지 출력
        return f"Error: {str(e)}"
