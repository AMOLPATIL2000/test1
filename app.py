from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('first.html')    
   
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")    
    app.run()
