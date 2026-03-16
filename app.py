from flask import Flask , render_template , request , url_for , jsonify
app = Flask(__name__)
from handle_DB import DB
from redirect import go_us,go_uk,go_de

# data base implementation
db = DB('codes.db')
db.create_table('codes(code varchar(8) , site varchar(15) , is_active boolean DEFAULT 1)')

from flask import g

@app.route("/")
def home():
     return render_template('index.html' , title = 'Flask')

@app.route('/check_code' , methods = ['POST'])
def check_code():
     code = request.get_json()
     checked = db.check_code(code['code'])
     if checked:
          return render_template('regist.html' , title = checked , code = code['code'])
     else:
          return jsonify({'code':code['code'],'is_active':False})


@app.route('/regist' , methods = ['POST'])
def regist():
     req = request.get_json()

     checked = db.check_code(req['code'])
     if checked:
            db.disable_code(code=req['code'])
            db.regist(req['code'],req['email'],req['first_name'],req['last_name'],req['state'])
            req['state'].replace(' ' , '+')
            if db.get_codeSite(req['code']) == 'life points':
                if req['country'] == 'uk':
                    return jsonify({'code':req['code'],'is_active':True,'country_found':True , 'redirect':go_uk(req)})
                elif req['country'] == 'usa':
                    return jsonify({'is_active':True,'country_found':True , 'redirect':go_us(req)})
                elif req['country'] == 'de':
                    return jsonify({'is_active':True,'country_found':True , 'redirect':go_de()})

     else:
          return jsonify({'code':req['code'],'is_active':False})
@app.route('/login_admin',methods=['POST','GET'])
def login_admin():
    return render_template('login.html')

@app.route('/dashboard_admin' , methods = ['POST'])
def dashboard():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(data)
    if db.check_admin(username,password):
        return render_template('dashboard.html' , registerations = db.get_registerations(10))
    return jsonify({'correct':False})
@app.route('/api/generate' , methods = ['POST'])
def add_codes_by_costumers():
     data = request.get_json()
     quantity = data['quantity']
     site = data['site']
     try:
         added_codes = added_codes = db.add_codes(site , quantity)
         return jsonify({'status':200,"quantity":quantity , 'codes':added_codes})
     except:
         return jsonify({'status':500})
if __name__ == "__main__":
    app.run(debug=True)