from flask import Flask, render_template, url_for, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route("/")
def index():
    Loan_amount = 10000
    # percent = lambda part, whole:float(whole) / 100 * float(part)
    # Annual interest rate for this loan
    Interest_rate=6.9
    # Monthly payment for this loan
    Monthly_payment = 0
    # Number of months for this loan
    Term_in_months = 120
    
    ED_LOAN = (Interest_rate/360)*(365/12)
    ED_INTERST = Interest_rate/360
    
    value = Loan_amount / ( (1/ED_LOAN) - (1/ ED_LOAN * (1 + ED_LOAN)**Term_in_months))
    v1=Loan_amount/((1/ED_LOAN)-(1/(((ED_LOAN*(1+ED_LOAN)**Term_in_months)))))
    return print(v1)
    # 	return render_template("index.html")

if __name__ == "__main__":
	app.run()
