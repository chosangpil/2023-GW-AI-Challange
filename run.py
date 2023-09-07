from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)


# 메인 페이지 라우팅
@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')

if __name__=="__main__":

  # 서비스 start
  app.run(debug=True, host='127.0.0.1', port=5000)
  
  # host 등을 직접 지정 가능
  # app.run(host="127.0.0.1", port="5000", debug=True)