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

Upon providing the transaction data, it will be sent to an API endpoint for the computation of the max rewards by month, which will then be displayed on the page. <!---![Screenshot - 2023-05-24T222738 425](https://github.com/jas6zhang/Capital-One-Technical/assets/65873016/f3ee1448-b710-4530-8c4b-2aced1bc2610)-->
*Note that the points by each transaction is not displayed due to usability for (imaginary) consumers. To compute the max points for each indvidual data, please go see the Testing Section in this markdown page. 

### Backend: 
In reward_calculator.py, the class `RewardCalculator` contains the logic to compute both the maximum reward points per transaction and for the entire month. 

The api.py file serves as the backend API server for the application, built using Flask. The function 'calculate_rewards' is decorated with ```@app.route('/calculate_rewards', methods=['POST'])```, handling HTTP POST requests sent to the endpoint containing the transaction data. It extracts the transaction data from the request JSON and passes it to the RewardCalculator class for reward calculation. The RewardCalculator class uses a greedy algorithm approach in order to give users the greatest amount of points. 

## Running the Program
### Frontend:

```cd frontend```
```cd app```

```npm i```

```npm start```

### Backend: 

```cd backend```

```pip3 install -r requirements.txt```

```python3 api.py```

The program is written in Python 3 so make sure the version is properly installed in your machine's environment. 

Please note that both the React and Flask server must be running at the same time for app to properly work. 

If simply to check that the program can calculate the reward amount, please read the testing section below. 

## Testing 
For a quick test to ensure that the basic requirements are satisfied, cd into the backend folder and run ```python reward_calculator.py```. 

This will return max rewards for each transaction and for the month using the default transactions provided. 
```
Rewards by Transaction: [({'points': 760}, {'rules_used': [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7]}), ({'points': 307}, {'rules_used': [6, 6, 6, 6, 7]}), ({'points': 3}, {'rules_used': [7]}), ({'points': 12}, {'rules_used': [7]}), ({'points': 21}, {'rules_used': [7]}), ({'points': 22}, {'rules_used': [7]}), ({'points': 18}, {'rules_used': [7]}), ({'points': 21}, {'rules_used': [7]}), ({'points': 238}, {'rules_used': [6, 6, 6, 7]}), ({'points': 13}, {'rules_used': [7]})]


Total Rewards for Month: ({'points': 1657}, {'rules_used': [1, 2, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7]})
```

Otherwise, feel free to include your own transaction data and run the program to drop it in!
