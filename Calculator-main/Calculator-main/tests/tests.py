
import sys
sys.path.append( "src" )
sys.path.append( "." )
from src.model.calculator import *
import unittest



class CalculatorTests(unittest.TestCase):
    # Casos de prueba válidos (hipoteca inversa vitalicia.)
    def test_case_1(self):
        total_amount = 650000000
        age = 71
        expected_life = 85
        fee_time = 1
        property_percentage = 1.5
        mortgage_type = 1

        expected = 58035.71428571428
        calc = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        result = calc.calculate_monthly_fee()

        self.assertAlmostEqual(expected, result, 2)

    def test_case_2(self):
        total_amount = 500000000
        age = 67
        expected_life = 80
        fee_time = 1
        property_percentage = 2
        mortgage_type = 1

        expected = 64102.5641025641
        calc = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        result = calc.calculate_monthly_fee()

        self.assertAlmostEqual(expected, result, 2)

    # Casos de prueba válidos (Hipoteca inversa Parcial.)
    def test_case_3(self):
        total_amount = 845000000
        age = 77
        expected_life = 80
        fee_time = 5
        property_percentage = 2.1
        mortgage_type = 2

        expected = 295750.0
        calc = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        result = calc.calculate_monthly_fee()

        self.assertAlmostEqual(expected, result, 2)

    def test_case_4(self):
        total_amount = 923000000
        age = 80
        expected_life = 95
        fee_time = 10
        property_percentage = 1.9
        mortgage_type = 2

        expected = 146141.66666666666
        calc = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        result = calc.calculate_monthly_fee()

        self.assertAlmostEqual(expected, result, 2)

    # Casos de prueba válidos (Hipoteca inversa total.)
    def test_case_5(self):
        total_amount = 900000000
        age = 70
        expected_life = 80
        fee_time = 1
        property_percentage = 1.2
        mortgage_type = 3

        expected = 10800000.0
        calc = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        result = calc.calculate_monthly_fee()

        self.assertAlmostEqual(expected, result, 2)

    def test_case_6(self):
        total_amount = 230000000
        age = 65
        expected_life = 70
        fee_time = 1
        property_percentage = 1.8
        mortgage_type = 3

        expected = 4140000.0000000005
        calc = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        result = calc.calculate_monthly_fee()

        self.assertAlmostEqual(expected, result, 2)

    # Casos de error.
    def test_amount_zero(self):
        total_amount = 0
        age = 65
        expected_life = 1
        fee_time = 1
        property_percentage = 5
        mortgage_type = 3

        self.assertRaises(InvalidAmount, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_negative_amount(self):
        total_amount = -250000000
        age = 65
        expected_life = 1
        fee_time = 1
        property_percentage = 5
        mortgage_type = 3

        self.assertRaises(InvalidAmount, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_age_zero(self):
        total_amount = 250000000
        age = 0
        expected_life = 1
        fee_time = 1
        property_percentage = 5
        mortgage_type = 1

        self.assertRaises(InvalidAge, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_invalid_age(self):
        total_amount = 150000000
        age = 60
        expected_life = 1
        fee_time = 1
        property_percentage = 5
        mortgage_type = 3

        self.assertRaises(InvalidAge, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_zero_expected_life(self):
        total_amount = 300000000
        age = 65
        expected_life = 0
        fee_time = 1
        property_percentage = 5
        mortgage_type = 3

        self.assertRaises(InvalidExpectedLife, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_negative_expected_life(self):
        total_amount = 330000000
        age = 70
        expected_life = -3
        fee_time = 1
        property_percentage = 4
        mortgage_type = 3

        self.assertRaises(InvalidExpectedLife, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_zero_fee_time(self):
        total_amount = 280000000
        age = 78
        expected_life = 1
        fee_time = 0
        property_percentage = 5
        mortgage_type = 3

        self.assertRaises(InvalidFeeTime, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_negative_fee_time(self):
        total_amount = 350000000
        age = 65
        expected_life = 1
        fee_time = -11
        property_percentage = 5
        mortgage_type = 3

        self.assertRaises(InvalidFeeTime, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_zero_property_percentage(self):
        total_amount = 130000000
        age = 65
        expected_life = 1
        fee_time = 1
        property_percentage = 0
        mortgage_type = 3

        self.assertRaises(InvalidPropertyPercentage, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_negative_property_percentage(self):
        total_amount = 770000000
        age = 80
        expected_life = 1
        fee_time = 1
        property_percentage = -3
        mortgage_type = 3

        self.assertRaises(InvalidPropertyPercentage, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_zero_option(self):
        total_amount = 500000000
        age = 69
        expected_life = 1
        fee_time = 1
        property_percentage = 1.5
        mortgage_type = 0

        self.assertRaises(InvalidOption, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)

    def test_negative_option(self):
        total_amount = 150000000
        age = 85
        expected_life = 1
        fee_time = 1
        property_percentage = 2
        mortgage_type = -3

        self.assertRaises(InvalidOption, Calculator, total_amount, age,
                          expected_life, fee_time, property_percentage, mortgage_type)


if __name__ == '__main__':
    unittest.main(verbosity=2)
