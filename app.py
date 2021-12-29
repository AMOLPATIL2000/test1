from flask import Flask,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('first.html')    

def get_prediction(exp):
          with open('model.data','rb') as f:
                    model = pickle.load(f)                    
          return model.predict([[exp]])[0]
 

@app.route('/getsalary',methods=['POST'])
def submit():
          if request.method=='POST':
                    exp = request.form['exp']
                    sal=get_prediction(float(exp))
          return str(sal)
   
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")    
    app.run()
