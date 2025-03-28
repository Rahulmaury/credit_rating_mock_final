# Credit Rating Agency - Residential Mortgage Securities (RMBS)

# Module imported
import json


# function definition
def calculate_credit_rating(morgage_collection):
    """It calculate Credit rating based on Mortgages input provide"""
    Average_credit_score_list = []
    Total_score_list = []
    for i in range(len(morgage_collection["mortgages"])):
        RiskScore = 0
        # 1. Loan-to-Value (LTV) Ratio:
        Numerator = morgage_collection["mortgages"][i]["loan_amount"]
        Denominator = morgage_collection["mortgages"][i]["property_value"]
        ltv = Numerator / Denominator
        if ltv > 0.9:
            RiskScore += 2
        elif ltv > 0.8:
            RiskScore += 1

        # 2. Debt-to-Income (DTI) Ratio:
        Numerator = morgage_collection["mortgages"][i]["debt_amount"]
        Denominator = morgage_collection["mortgages"][i]["annual_income"]
        dti = Numerator / Denominator

        if dti > 0.5:
            RiskScore += 2
        elif dti > 0.4:
            RiskScore += 1

        # 3. Credit Score:
        credit_score = morgage_collection["mortgages"][i]["credit_score"]
        if credit_score >= 700:
            RiskScore -= 1
        elif credit_score >= 650 and credit_score <= 700:
            pass
        elif credit_score < 650:
            RiskScore += 1

        # 4. Loan Type:
        loan_type = morgage_collection["mortgages"][i]["loan_type"]
        if loan_type == "fixed":
            RiskScore -= 1
        elif loan_type == "adjustable":
            RiskScore += 1

        # 5. Property Type:

        property_type = morgage_collection["mortgages"][i]["property_type"]
        if property_type == "condo":
            RiskScore += 1

        # 6. Average Credit Score:
        Average_credit_score_list.append(credit_score)
        # 7 Total Score:
        Total_score_list.append(RiskScore)

    Total_score = sum(Total_score_list)

    Average_credit_score = sum(Average_credit_score_list) / len(
        Average_credit_score_list
    )

    # Check Average Score to finalize Total_score
    if Average_credit_score >= 700:
        Total_score -= 1
    elif Average_credit_score < 650:
        Total_score += 1

    # Define Credit Rating based on Total_score
    if Total_score <= 2:
        return "AAA"
    elif Total_score >= 3 and Total_score <= 5:
        return "BBB"
    elif Total_score > 5:
        return "C"


if __name__ == "__main__":
    # Pass JSON Input to Function from File: input_file.json
    # Open the JSON file and load morgage_collection_json
    f = open("Input_file.json")
    morgage_collection_json = json.load(f)

    # Calling the function
    final_Rating = calculate_credit_rating(morgage_collection_json)
    print(final_Rating)
