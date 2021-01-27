import unittest2
from Payment_Gateway_Flask_WebAPI import ProcessPayment,check_conditions,Check_PaymentGateway_conditions,app
import requests
import sys
from Payment_Gateway_Flask_WebAPI import *


class Test_Flask_API_Using_Requests(unittest2.TestCase):
    def test_URL_with_security_code(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243442666782892&SecurityCode=657&CardHolder=AKSHAY&ExpirationDate=03-22&Amount=19.00")
        self.assertEqual(response.status_code, 200) 
        
    def test_URL(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243442666782892&CardHolder=AKSHAY&ExpirationDate=03-22&Amount=19.00")
        self.assertEqual(response.status_code, 200)
    
    def test_URL_for_creditcard(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243443222892&CardHolder=AKSHAY&ExpirationDate=03-22&Amount=250.00")
        self.assertEqual(response.status_code, 400)  
    
    def test_URL_for_CreditCardNumber(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243443222892789&ExpirationDate=03-22&Amount=250.00")
        self.assertEqual(response.status_code, 400)

    def test_URL_for_creditcardAbcent(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CardHolder=AKSHAY&ExpirationDate=03-22&Amount=250.00")
        self.assertEqual(response.status_code, 400)
        
    def test_ExpirationDate(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243443222427892&CardHolder=AKSHAY&ExpirationDate=03-19&Amount=250.00")
        self.assertEqual(response.status_code, 400)    
        
    def test_ExpirationDate_format(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243443222427892&CardHolder=AKSHAY&ExpirationDate=0322&Amount=250.00")
        self.assertEqual(response.status_code, 400)     
        
    def test_Amount(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243443222427892&CardHolder=AKSHAY&ExpirationDate=03-19")
        self.assertEqual(response.status_code, 400)  
        

    def test_URL_withour_security_code(self):
        response = requests.get("http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243442666782892&SecurityCode=65897&CardHolder=AKSHAY&ExpirationDate=03-22&Amount=19.00")
        self.assertEqual(response.status_code, 400)         
    
    def test_apiroute_ProcessPayment(self):
        adapter = app.url_map.bind('')
        adapter.match('/ProcessPayment')
    
    def test_apiroute_ProcessPayment_CheapPaymentGateway(self):
        adapter = app.url_map.bind('')
        adapter.match('/ProcessPayment/CheapPaymentGateway', method = 'GET')
    
    def test_apiroute_ProcessPayment_ExpensivePaymentGateway(self):
        adapter = app.url_map.bind('')
        adapter.match('/ProcessPayment/ExpensivePaymentGateway', method = 'GET')
    
    def test_apiroute_ProcessPayment_PremiumPaymentGateway(self):
        adapter = app.url_map.bind('')
        adapter.match('/ProcessPayment/PremiumPaymentGateway', method = 'GET')
    


if __name__ == '__main__':
    unittest2.main(verbosity = 2)