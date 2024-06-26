# KDT_Team1_Flask_TP
<br>1조 flask 팀프로젝트 : 딥러닝 모델 기반 쓰레기 분류 해주는 웹사이트 구축</br>
<br>조원 : 권혁원, 우승연, 이화은</br>
<br>주제 설명 : 현대에는 매우 많은 양의 쓰레기가 배출되고 있다. 효율적인 쓰레기 배출을 위해서는 분리수거가 잘 이루어져야 하지만, 배출 기준이 모호하다</br>
<br></br>
![image](https://github.com/Skylee0310/KDT_Flask/assets/155412049/8bf8f173-1991-481c-9ced-15148aed026f)

## 조원별 세부 계획
|조원|내용|
|:---|:---:|
|권혁원|재활용품 이미지 종류별 분류 모델|
|우승연|일반쓰레기/재활용쓰레기 이미지 분류 모델|
|이화은|일반쓰레기/음식물쓰레기 이미지 분류 모델|


<details>
<summary> 이화은
</summary>
<div markdown="1">
  
### 📝 주제 - 쓰레기 분류

✏ **주제 선정 배경**

- 교육장 내에서도 많은 양의 쓰레기가 매일 배출되고 있음.
- 환경을 위해 쓰레기를 분리배출해야 하지만 배출 기준이 모호함.
- 쓰레기를 사진으로 찍으면 배출 방법을 알려주는 서비스

![image](https://github.com/Skylee0310/KDT_Flask/assets/155412049/f9973346-dc72-49a3-9b74-4a3c6b0b78ce)


| 📄 개인 주제 | 음식물 쓰레기와 일반 쓰레기 분류 모델 |
| --- | --- |
| 🙍🏻‍♂️ 팀원 | 권혁원, 우승연, 이화은 |
| 📊 PPT | https://buly.kr/28rLeCI |

➕ 변경 주제 : 과일 중 그대로 음식물 쓰레기로 버릴 수 있는 것과 안 되는 것 분류.

✏ **개인** **주제 선정 배경**

![image](https://github.com/Skylee0310/KDT_Flask/assets/155412049/6ad5e767-d41b-4ca5-bd30-eebcda16446e)

- 음식물 쓰레기 - 일반 쓰레기 구분 모호 ⇒  **혼선 발생**
- 지역마다 기준이 상이함.
⇒ 이 때문에 대구광역시 기준 음식물 쓰레기와 아닌 것을 분류하여 불편함을 해소하고자 함

✏  **자료 수집 및 가공** **방법  :**

- 대구광역시 홈페이지에서 음식물 쓰레기로 분류하기 쉬운 일반 쓰레기 자료를 다운로드.
    - https://www.daegu.go.kr/env/index.do?menu_id=00001320

- **캐글**에서 다운로드
    - **Real-Image Datasets -**  Food Organics
    - **Garbage Image Dataset** - Food
- 크롬 확장 프로그램을 이용하여 음식 사진을 다운 받아 음식물 쓰레기, 일반 쓰레기 라벨링
- 사진 데이터 양이 모자라서 샘플링.
- CNN 모델을 사용하여 사진 파일을 처리.
- 분류가 잘 되지 않아 사진을 크롭

✏  **과정 :**

- **1일차(0419) :**
    - 주제 선정 (쓰레기 분류)
    - 데이터셋 다운로드 후 눈으로 보면서 재분류

✏  **주의 :** 

- 가능한 한 클래스 간 차이가 크지 않도록 할 것. (**데이터 불균형**)

✏  **문제 및 시행 착오 :**

- Real-Image Datasets의 Food Organics폴더 사용 but 비닐, 티백, 파인애플, 생선뼈 등 일반 쓰레기가 섞여있어 사진을 보면서 기준에 따라 재분류 (하드 코딩)
- 캐글에서 다운 받은 데이터 개수가 절대적으로 부족
- 데이터를 구글에서 다운 받는데 음식의 경우 일반 쓰레기로 분류되어야 하는 것이 섞여있으면 사용할 수 없고 기준이 모호해서 어떻게 버려야 하는지 애매한 것들이 많음.
    - 조개가 들어가지 않은 국이나 파스타 쪽으로 음식 사진을 수집.
    - 빵 사진 수집.
    - 과일 중 껍질까지 음식물 쓰레기로 버릴 수 있는 것을 음식물 쓰레기로 분류.
- 파일명이 한글로 되어있어서 인지 오류가 발생하여 코드가 돌아가지 않았음.
    - 이지네이머를 사용하여 파일명 확장자 일괄 변경.
- 분류 부정확( 0421 오전 )
- 과일로 범위를 축소.

✏  **결론 제언 :**

- 음식물 쓰레기와 일반 쓰레기 분류하는 기준이 모호하기 때문에 분류가 어렵다.
- 쓰레기를 바르게 버리는 것도 중요하지만 배출량 자체를 줄이는 것이 효과적.
- 음식물 쓰레기를 줄이는 방법 : http://www.realfoods.co.kr/view.php?ud=20231128000161

✏  **Web**
![image](https://github.com/Skylee0310/KDT_Flask/assets/155412049/83ae21fd-e063-4cd6-8805-7f8893844ea3)

<br></br>

![image](https://github.com/Skylee0310/KDT_Flask/assets/155412049/c18d89a3-8ec6-4596-8479-7a387431c0d8)

</div>
</details>
