from typing import Any, Dict, List, Set, Tuple  # for typing hints

# default given rules
RULES = [
    {"rule_num": 1,
    "points": 500,
     "limits": [("sportcheck", 75), ("tim_hortons", 25), ("subway", 25)]
     },
    {
    "rule_num": 2,
    "points": 300,
     "limits": [("sportcheck", 75), ("tim_hortons", 25)]
     },
    {
     "rule_num": 3,
     "points": 200,
     "limits": [("sportcheck", 75)]
     },
    {
     "rule_num": 4,
     "points": 150,
     "limits": [("sportcheck", 25), ("tim_hortons", 10), ("subway", 10)]
     },
    {
     "rule_num": 5,
     "points": 75,
     "limits": [("sportcheck", 25), ("tim_hortons", 10)]
     },
    {
     "rule_num": 6,
     "points": 75,
     "limits": [("sportcheck", 20)]
     },
    {
     "rule_num": 7,
     "points": 1,
     "limits": [("other", 1)]
     },
]

# add additional merchant names to list if need be
KNOWN_MERCHANTS = {
    "sportcheck",
    "tim_hortons",
    "subway",
    "other"
}

# sample transaction input
TRANSACTIONS = {
    "T01": {"date": "2021-05-01", "merchant_code": "sportcheck", "amount_cents": 21000},
    "T02": {"date": "2021-05-02", "merchant_code": "sportcheck", "amount_cents": 8700},
    "T03": {"date": "2021-05-03", "merchant_code": "tim_hortons", "amount_cents": 323},
    "T04": {"date": "2021-05-04", "merchant_code": "tim_hortons", "amount_cents": 1267},
    "T05": {"date": "2021-05-05", "merchant_code": "tim_hortons", "amount_cents": 2116},
    "T06": {"date": "2021-05-06", "merchant_code": "tim_hortons", "amount_cents": 2211},
    "T07": {"date": "2021-05-07", "merchant_code": "subway", "amount_cents": 1853},
    "T08": {"date": "2021-05-08", "merchant_code": "subway", "amount_cents": 2153},
    "T09": {"date": "2021-05-09", "merchant_code": "sportcheck", "amount_cents": 7326},
    "T10": {"date": "2021-05-10", "merchant_code": "tim_hortons", "amount_cents": 1321}
}


class RewardCalculator:
    def __init__(self,
                 transactions: Dict[str, Dict[str, Any]] = TRANSACTIONS,
                 rules: List[Dict[str, Any]] = RULES,
                 known_merchants: Set[str] = KNOWN_MERCHANTS
                 ):
        self.transactions = transactions
        self.rules = rules
        self.known_merchants = known_merchants
        self.remove_unoptimal_rules()
        self.read_transactions()

    def read_transactions(self):
        
        # formatted transactions with list of only merchant and amount
        formmated_transactions = []
      
        # group transactions by merchant for monthlycalculation
        monthly_transactions_by_merchant = {
            merchant: 0.0 for merchant in self.known_merchants}

        # go through each transaction
        for transaction in self.transactions.values():
            merchant = transaction["merchant_code"]

            if merchant not in self.known_merchants:
                merchant = "other"

            amount = transaction["amount_cents"] / 100
            
            formmated_transactions.append({merchant: amount})

            monthly_transactions_by_merchant[merchant] += amount
        
        self.formmated_transactions = formmated_transactions
        self.monthly_transactions = monthly_transactions_by_merchant

    def remove_unoptimal_rules(self):
        # Idea: Using Greedy Strategy -> always use the rule that gives the most points if resources are sufficient
        # Rules 3/5 gives more points, but they also use more resources per dollar vs. other existing rules with the exact same merchants
        # Therefore, should remove rules 3/5 to fit solution to greedy structure and get a more optimal result
        
        self.rules = [rule for rule in self.rules if rule["rule_num"] not in {3, 5}]

    # apply Greedy 
    def max_rewards_for_transaction(self, transaction):
        rewards = 0
        rules_used = []

        # priotize rules that give the most points
        for rule in sorted(self.rules, key=lambda rule: rule["points"], reverse=True):
            
            # compute how many times rule can be applied
            while self.can_apply_rule(transaction, rule["limits"]):
                for merchant, dollars_spent in rule["limits"]:
                    transaction[merchant] -= dollars_spent
                    
                rewards += rule["points"]
                rules_used.append(rule["rule_num"]) 

        # add remaining amount to "other" after going through all of the rules
        remaining_amount = sum(transaction.values())
        if remaining_amount > 0:
            transaction["other"] = remaining_amount

            # assuming the last rule is for "other"
            rule_for_other = self.rules[-1]
            
            if self.can_apply_rule(transaction, rule_for_other["limits"]):
                transaction["other"] -= remaining_amount
                rewards += rule_for_other["points"] * \
                    int(remaining_amount // rule_for_other["limits"][0][1]) 
                
                # add the given points for each dollar used in the "other" rule (default is 1 point/dollar)
                    
                if rule_for_other["rule_num"] not in rules_used:
                    rules_used.append(rule_for_other["rule_num"])

        return {"points": rewards}, {"rules_used": rules_used}

    def max_points_by_transaction(self) -> List[Tuple[int, Dict[str, List[int]]]]:
        max_rewards = []
        
        # return list of points for each transaction if they were computed seperately

        for count, transaction in enumerate(self.formmated_transactions):
            max_reward = self.max_rewards_for_transaction(transaction)
            
            max_rewards.append({"T" + str(count + 1): max_reward})

        return max_rewards

    def max_points_for_month(self) -> Tuple[int, Dict[str, List[int]]]:

        # return list of points for transactions if they were grouped together
        return self.max_rewards_for_transaction(self.monthly_transactions)

    def can_apply_rule(self, transaction, limits):
        for merchant, limit in limits:
            if transaction.get(merchant, 0) < limit: # return 0 if merchant not in transaction to prevent access error
                return False
        return True
    
def testing():
    print("Rewards by Transaction:",
            RewardCalculator().max_points_by_transaction())
    print("Total Rewards for Month:",
            RewardCalculator().max_points_for_month())


testing()  # displays raw data for default inputs in the cmd line 
