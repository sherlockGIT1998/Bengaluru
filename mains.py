from flask import Flask,render_template,request

from utils import BengaluruHousePrice

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Bengaluru House Price Prediction...')
    return render_template('index.html')

@app.route('/predict_prices',methods=['POST','GET'])
def price_info():
    if request.method == 'GET':
        print('GET Method...')
        
        # data = request.form 
        # area_type = data['area_type']
        # availability = data['availability']
        # location = data['location']
        # size = data['size']
        # total_sqft = data['total_sqft']
        # bath = eval(data['bath'])
        # balcony = eval(data['balcony'])
        
        area_type = request.args.get('area_type')
        availability = request.args.get('availability')
        location = request.args.get('location')
        size = request.args.get('size')
        total_sqft = request.args.get('total_sqft')
        bath = eval(request.args.get('bath'))
        balcony = eval(request.args.get('balcony'))
        
        
        price = BengaluruHousePrice(area_type,availability,location,size,total_sqft,bath,balcony)
        
        predict = price.get_predicted_prices()
        
        return render_template('index.html',prediction=round(predict,2))
        # return f'Pricce of Bengaluru House is : Rs.{round(predict,2)} Lakh/-'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    app.run()