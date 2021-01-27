# PaymentGatewayAPI
This is flask WebAPI for Process Payment, and once all the details are satisfied, it forward to third party payment gateway based on the the amount to be processed.

Thier are two main files.

## Payment_Gateway_Flask_WebAPI
This consist of main python flask API script for processing the payment based on the given condition.

## Unit_Testing
This is to test script to test all the conditions and the response, as well as the app routes.

## Executing the Script
After running the flask webapi script on the host at 5000 port. kindly check the URl for the testing.
```
http://127.0.0.1:5000/ProcessPayment?CreditCardNumber=1243442666782892&SecurityCode=657&CardHolder=FILED&ExpirationDate=03-22&Amount=19.00

```
