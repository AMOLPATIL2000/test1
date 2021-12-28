from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
   return "<h1>Hello</h1>"     
   
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")    
    app.run()