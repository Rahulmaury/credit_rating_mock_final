import unittest
import credit_rating

Test_AAA = {
    "mortgages": [
        {
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family",
        },
        {
            "credit_score": 680,
            "loan_amount": 150000,
            "property_value": 175000,
            "annual_income": 45000,
            "debt_amount": 10000,
            "loan_type": "adjustable",
            "property_type": "condo",
        },
    ]
}

Test_BBB = {
    "mortgages": [
        {
            "credit_score": 650,
            "loan_amount": 230000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family",
        },
        {
            "credit_score": 680,
            "loan_amount": 150000,
            "property_value": 175000,
            "annual_income": 45000,
            "debt_amount": 10000,
            "loan_type": "adjustable",
            "property_type": "condo",
        },
    ]
}

Test_C = {
    "mortgages": [
        {
            "credit_score": 650,
            "loan_amount": 230000,
            "property_value": 50000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "adjustable",
            "property_type": "condo",
        },
        {
            "credit_score": 680,
            "loan_amount": 150000,
            "property_value": 175000,
            "annual_income": 45000,
            "debt_amount": 10000,
            "loan_type": "adjustable",
            "property_type": "condo",
        },
    ]
}


class Test_credit_rating(unittest.TestCase):

    def test_AAA(self):
        result = credit_rating.calculate_credit_rating(Test_AAA)
        self.assertEqual(result, "AAA")

    def test_BBB(self):
        result = credit_rating.calculate_credit_rating(Test_BBB)
        self.assertEqual(result, "BBB")

    def test_C(self):
        result = credit_rating.calculate_credit_rating(Test_C)
        self.assertEqual(result, "C")


if __name__ == "__main__":
    unittest.main()
