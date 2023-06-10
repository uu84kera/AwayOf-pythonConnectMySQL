from flask import Flask,request,render_template
from flask_cors import CORS
import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',password='password',database='matching',charset='utf8')
app = Flask(__name__)

CORS(app)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/questionnaire",methods = ["GET","POST"])
def questions():
    if request.method == "GET":
        return render_template('questionnaire.html')
    elif request.method =='POST':
        data = request.form
        print('--->upload form data: ',data)
        name=data.get('name')
        gender = data.get('gender')
        zuoxi=data.get('zuoxi')
        shejiao=data.get('shejiao')
        jiepi = data.get('jiepi')
        xizao = data.get('xizao')
        yifu=data.get('yifu')
        weisheng=data.get('weisheng')
        ciji=data.get('ciji')
        youxi=data.get('youxi')
        shengyin=data.get('shengyin')
        kongtiao=data.get('kongtiao')
        xingqu = data.get('xingqu')
        add_name_db(name,gender,zuoxi,shejiao,jiepi,xizao,yifu,weisheng,ciji,youxi,shengyin,kongtiao,xingqu)


        v3 = data.get('v3')
        v4 = data.get('v4')
        v5 = data.get('v5')
        v6 = data.get('v6')

        v8 = data.get('v8')
        v9= data.get('v9')
        v10 = data.get('v10')
        v11 = data.get('v11')
        v12 = data.get('v12')
        v13 = data.get('v13')
        add_data_db(name,v3,v4,v5,v6,v8,v9,v10,v11,v12,v13)

        return "Thanks for joining!"

def add_name_db(name,gender,zuoxi,shejiao,jiepi,xizao,yifu,weisheng,ciji,youxi,shengyin,kongtiao,xingqu):
    with conn.cursor() as c:
        sql = "insert into matching1(name,gender,zuoxi,shejiao,jiepi,xizao,yifu,weisheng,ciji,youxi,shengyin,kongtiao,xingqu) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql, args=(name,gender,zuoxi,shejiao,jiepi,xizao,yifu,weisheng,ciji,youxi,shengyin,kongtiao,xingqu))
        conn.commit()

def add_data_db(name,v3,v4,v5,v6,v8,v9,v10,v11,v12,v13):
    with conn.cursor() as c:
        sql = "insert into matching2(name,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql, args=(name,v3,v4,v5,v6,v6,v8,v9,v10,v11,v12,v13))
        conn.commit()

if __name__ == '__main__':
    app.run(debug=True)
