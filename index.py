from flask import Flask, render_template, request, Response
import sys
import cv2
from time import sleep

app = Flask(__name__)
capture = cv2.VideoCapture(0)  # 웹캠으로부터 비디오 캡처 객체 생성
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 캡처된 비디오의 폭 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 캡처된 비디오의 높이 설정

def GenerateFrames():
    while True:
        sleep(0.1)  # 프레임 생성 간격을 잠시 지연시킵니다.
        ref, frame = capture.read()  # 비디오 프레임을 읽어옵니다.
        if not ref:  # 비디오 프레임을 제대로 읽어오지 못했다면 반복문을 종료합니다.
            break
        else:
            ref, buffer = cv2.imencode('.jpg', frame)  # JPEG 형식으로 이미지를 인코딩합니다.
            frame = buffer.tobytes()  # 인코딩된 이미지를 바이트 스트림으로 변환합니다.
            # multipart/x-mixed-replace 포맷으로 비디오 프레임을 클라이언트에게 반환합니다.
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/',  methods=['GET', 'POST'])

@app.route('/')
def index(): 

    remote = ""

    if request.method == 'POST':
        remote = request.form.get("remote")
        print(remote)
        
    # return render_template('index.html', remotePrint = remote)
    return render_template('index.html')
    

@app.route('/stream')
def Stream():
    # GenerateFrames 함수를 통해 비디오 프레임을 클라이언트에게 실시간으로 반환합니다.
    return Response(GenerateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run()
