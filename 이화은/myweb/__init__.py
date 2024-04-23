## 모듈 로딩
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

## DB관련 인스턴스 생성 
db = SQLAlchemy() # 전역 변수
migrate = Migrate() # 전역 변수


def create_app() :
    app = Flask(__name__)
    
    # 성정 내용 로딩 (파이선 파일에서 읽어들인다.)
    app.config.from_pyfile('config.py')

    # ORM 즉, DB 초기화 -> db객체를 create_app 안에서 생성하면 블루프린트와 같은 다른 모듈에서 불러올 수 없기 때문에 밖에서 생성.
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import foodmdl

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app