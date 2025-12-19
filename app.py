from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, jsonify
import requests
from tools import fetch_products
from chain import run_chain
app=Flask(__name__)
FAKE_STORE="https://fakestoreapi.com/products"
@app.route("/")
def home():
    response=requests.get(FAKE_STORE)
    products=response.json()
    return render_template("home.html",products=products)
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    products = fetch_products(user_msg)

    response = run_chain(user_msg, products)
    return jsonify({"reply": response})
if __name__=="__main__":
    app.run(debug=True)