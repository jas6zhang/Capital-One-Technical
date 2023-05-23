# Capital One Technical Assessment
This is my implementation of the Credit Card Reward Points Calculator Technical Assesment for Capital One. To display the max reward points for the user, I created a fun frontend React interface integrated with a Flask API server. Please feel free to test it out! 

## App Structure
The app is seperated into the frontend and backend folders. 

### Frontend: 
The frontend is built using React, and allows the user to drop/select a JSON file containing custom transaction data (if they so choose). The data must be formatted according to the sample transaction data provided on the assessment documentation page: 

ex.
```
{
    "transactions": {
        "T01": { "date": "2021-05-01", "merchant_code": "sportcheck", "amount_cents": 21000 },
        "T02": { "date": "2021-05-02", "merchant_code": "sportcheck", "amount_cents": 8700 },
        "T03": { "date": "2021-05-03", "merchant_code": "tim_hortons", "amount_cents": 323 },
        "T04": { "date": "2021-05-04", "merchant_code": "tim_hortons", "amount_cents": 1267 },
        "T05": { "date": "2021-05-05", "merchant_code": "tim_hortons", "amount_cents": 2116 },
        "T06": { "date": "2021-05-06", "merchant_code": "tim_hortons", "amount_cents": 2211 },
        "T07": { "date": "2021-05-07", "merchant_code": "subway", "amount_cents": 1853 },
        "T08": { "date": "2021-05-08", "merchant_code": "subway", "amount_cents": 2153 },
        "T09": { "date": "2021-05-09", "merchant_code": "sportcheck", "amount_cents": 7326 },
        "T10": { "date": "2021-05-10", "merchant_code": "tim_hortons", "amount_cents": 1321 }
    }
}
```

Upon providing the transaction data, it will be sent to an API endpoint for the computation of the max rewards by month, which will then be displayed on the page. 

### Backend: 
In reward_calculator.py, the class `RewardCalculator` contains the logic to compute both the maximum reward points per transaction and for the entire month. 

The api.py file serves as the backend API server for the application, built using Flask. The function 'calculate_rewards' is decorated with @app.route('/calculate_rewards', methods=['POST']) to handle HTTP POST requests sent to the endpoint containing the transaction data. It extracts the transaction data from the request JSON and passes it to the RewardCalculator class for reward calculation.

## Running the Program
### Frontend:

```cd frontend```

```npm i```

```npm start```

### Backend: 

```cd backend```

```pip3 install -r requirements.txt```

```python3 api.py```

The program is written in Python 3 so make sure the version is properly installed in your machine's environment. 

Please note that both the react and flask server must be running at the same time for app to properly work. 

## Testing 
For a quick test to ensure that the basic requirements are satisfied, cd into the backend folder and run ```python reward_calculator.py```. 

This will return max rewards for each transaction and for the month using the default transactions provided. 

Otherwise, feel free to include your own transaction data and run the program to drop it in!
