from flask import Flask
from flask import request, jsonify, Response, abort, redirect, session, url_for
from flask_restful import Resource,Api, reqparse
import datetime
import requests

#requests.adapters.DEFAULT_RETRIES = 3

now = datetime.datetime.now()
present_month = now.strftime("%m-%y")

class Check_PaymentGateway_conditions():
    
    def Check_cheap_payment_gateway():
        return redirect(url_for('CheapPaymentGateway',**request.args))
    
    def Check_exprensive_payment_gateway():
        adapters = app.url_map.bind('')
        try:
            if adapters.match('/ProcessPayment/ExpensivePaymentGateway'):
                return redirect(url_for('ExpensivePaymentGateway',**request.args))
        except:
            return redirect(url_for('CheapPaymentGateway',**request.args))
      
    def Check_premium_payment_gateway():
            for i in range(3):
                try:
                   return redirect(url_for('PremiumPaymentGateway'))
                   break
                except Exception:
                    continue



class check_conditions():
    def security_code(amount_length):
        try:
            if amount_length:       
                if not len(str(amount_length)) == 3:
                    raise ValueError
        except ValueError:
            abort(400," Inappropiate security code")
        else:
            return amount_length

    def amount_check(amount_value):
        try:
            if not amount_value > 0:
                raise ValueError
        except ValueError:
            abort(400, " The given amount is inappropiate value")
        else :
            return amount_value  

    def credit_card_check(credit_card_as_string):
        try:
            if not credit_card_as_string.isdigit():
                raise ValueError
            if not len(credit_card_as_string) == 16:
                raise ValueError
        except ValueError:
            abort(400, " The credit card detials is not Numerical")
        except ValueError:
            abort(400, " The entered credit card detials is inappropiate ")
        else:
            return credit_card_as_string
      
    def date_format(date_as_string):
        try:
            if datetime.datetime.strptime(date_as_string, '%m-%y') < datetime.datetime.strptime(present_month,'%m-%y'):
                raise ValueError
        except ValueError:
            abort(400, " The card is expired ")
        else:
            return date_as_string

 
app = Flask(__name__)
api = Api(app)


class ProcessPayment(Resource):

    @app.route('/ProcessPayment')
    def Url_define_Query():
        if not request.args.get("CreditCardNumber"):           
            abort(400, " The CreditCardNumer is missing")
        
        if not request.args.get("CardHolder"):           
            abort(400, "The Card Holder name is missing")
        
        if not request.args.get("ExpirationDate"):           
            abort(400, "The Expiration Date is missing")
            
        if not request.args.get("Amount"):           
            abort(400, "Missing Amount")

        Credit_Card_Number = check_conditions.credit_card_check(request.args.get('CreditCardNumber', type = str))
        Card_Holder = request.args.get('CardHolder', type = str)
        Expiration_Date = check_conditions.date_format(request.args.get('ExpirationDate'))
        Security_Code = check_conditions.security_code(request.args.get('SecurityCode',None, type = int))
        Amount = check_conditions.amount_check(request.args.get('Amount', type = float))
       
        
        if Amount < 20.00:
            return Check_PaymentGateway_conditions.Check_cheap_payment_gateway()
        
        elif (Amount >= 21.00 and Amount <= 500.00):
            return Check_PaymentGateway_conditions.Check_exprensive_payment_gateway()
            
        elif Amount > 500.00:    
            return Check_PaymentGateway_conditions.Check_premium_payment_gateway()  
       
        else: 
            return 'Value need to defined in the catogery', 400


    @app.route('/ProcessPayment/CheapPaymentGateway', methods = ['GET'])
    def CheapPaymentGateway():
        return "Your Payment is processed to CheapPaymentGateway", 200
    
    @app.route('/ProcessPayment/ExpensivePaymentGateway', methods = ['GET'])
    def ExpensivePaymentGateway():
        return " Your Payment is processed to ExpensivePaymentGateway", 200
        

    @app.route('/ProcessPayment/PremiumPaymentGateway', methods = ['GET'])
    def PremiumPaymentGateway():
        return " Your Payment is processed by PremiumPaymentGateway ", 200
    

if __name__ == "__main__":
    app.run(debug=True, port = 5000)