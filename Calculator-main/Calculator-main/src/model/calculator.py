"""
Desarrollar una calculadora que permita calcular la cuota mensual que un banco le pagaría a una persona que ha adquirido
una hipoteca inversa.
"""

MINIMUM_AGE = 65
LIFE_MORTGAGE = 1
PARTIAL_MORTGAGE = 2
TOTAL_MORTGAGE = 3
VALIDS_INPUTS = [LIFE_MORTGAGE, PARTIAL_MORTGAGE, TOTAL_MORTGAGE]


class InvalidAmount(Exception):
    """
    Custom exception for invalids amounts

    Excepcion personalizada para indicar que el monto no cumple con los requerimientos.
    """

    def __init__(self):
        super().__init__(f'El valor de la propiedad no cumple con los requerimientos minimos para acceder a una '
                         f'hipoteca inversa.')


class InvalidAge(Exception):
    """
    Custom exception for invalid ages.

    Excepción personalizada para aquellas edades que no cumplen cons los requerimientos minimos para acceder a una
    hipoteca inversa.
    """

    def __init__(self):
        super().__init__(
            f'La edad ingresada no cumple con los requerimientos minimos para acceder a una hipoteca inversa. '
            f'Por favor, tenga en cuenta que solo los adultos mayores con una edad igual o mayor a 65 pueden '
            f'acceder al beneficio.')


class InvalidExpectedLife(Exception):
    """
    Custom exception for invalid life expectancies (equal to or less than zero).

    Excepción personalizada para las esperanzas de vida no validas (iguales o menores que cero)
    """

    def __init__(self):
        super().__init__(f'La esperanza de vida ingresada no cumple con los requerimientos minimos. '
                         f'Por favor, tenga en cuenta que la esperanza de vida debe ser mayor que cero.')


class InvalidFeeTime(Exception):
    """
    Custom exception for invalid payment periods (equal to or less than zero).

    Excepción personalizada para periodos de pago no validos (iguales o menores que cero).
    """

    def __init__(self):
        super().__init__(f'El periodo de pago ingresado no cumple con los requerimientos minimos. Tenga en '
                         f'cuenta que el periodo de pago debe ser mayor que cero.')


class InvalidPropertyPercentage(Exception):
    """
    Custom exception for invalids property percentage (equal to or less than zero).

    Excepción personalizada para porcentajes de propiedad no válidos (iguales o menores que cero).
    """

    def __init__(self):
        super().__init__(f'El porcentaje de propiedad ingresado no cumple con los requerimientos minimos. Tener '
                         f'en cuenta que el porcentaje de propiedad debe ser mayor que cero.')


class InvalidOption(Exception):
    """
    Custom exception for invalids user inputs.

    Excepción personalizada para entradas de usuario no validas.
    """

    def __init__(self):
        super().__init__(f'La opción ingresada no es válida. Por favor, seleccione nuevamente.')


class ExpectedLifeEqualToAge(Exception):
    """
    Custom exception for expected life less or equal than age.

    Excepción personalizada para expectativa de vida menor o igual que la edad.
    """

    def __init__(self):
        super().__init__(f'La expectativa de vida no puede ser igual o menor que la edad.')


class Calculator:
    def __init__(self, total_amount: int, age: int, expected_life: int, fee_time: int,
                 property_percentage: float, mortgage_type: int):
        """
        Initialize the ReverseMortgageCalculator with parameters.

        Args:
            total_amount (int): The total amount of the mortgage.
            age (int): The age of the mortgage holder.
            expected_life (int): The expected life of the mortgage holder.
            fee_time (int): The time period for fees.
            property_percentage (float): The percentage of the property value.
            mortgage_type (int): Type of mortgage (1, 2, or 3).

        Raises:
            InvalidAmount: If the total_amount is not within the valid range.
            InvalidAge: If the age is less than the minimum required age.
            InvalidExpectedLife: If the expected_life is less than or equal to zero.
            InvalidFeeTime: If the fee_time is less than or equal to zero.
            InvalidPropertyPercentage: If the property_percentage is less than or equal to zero.
            InvalidOption: If the mortgage_type is not a valid option.
        """

        self._validate_inputs(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)

        self.total_amount: int = total_amount
        self.age: int = age
        self.expected_life: int = expected_life
        self.fee_time: int = fee_time
        self.property_percentage: float = property_percentage
        self.mortgage_type: int = mortgage_type

    @staticmethod
    def _validate_inputs(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type):
        if total_amount <= 0:
            raise InvalidAmount()

        if age < MINIMUM_AGE:
            raise InvalidAge()

        if expected_life <= 0:
            raise InvalidExpectedLife()

        if fee_time <= 0:
            raise InvalidFeeTime()

        if property_percentage <= 0:
            raise InvalidPropertyPercentage()

        if mortgage_type not in VALIDS_INPUTS:
            raise InvalidOption()

        if expected_life <= age:
            raise ExpectedLifeEqualToAge()

    def calculate_monthly_fee(self) -> float:
        """
        Calculate the monthly fee or payment based on mortgage type.

        Returns:
            float: The calculated monthly fee or payment.
        """

        property_percentage_adjusted = self.property_percentage / 100

        if self.mortgage_type == LIFE_MORTGAGE:
            income_years = self.expected_life - self.age
            income_months = income_years * 12
            total_amount = self.total_amount * property_percentage_adjusted
            monthly_fee = total_amount / income_months
            return monthly_fee
        elif self.mortgage_type == PARTIAL_MORTGAGE:
            fee_time = self.fee_time * 12
            total_amount = self.total_amount * property_percentage_adjusted
            monthly_fee = total_amount / fee_time
            return monthly_fee
        elif self.mortgage_type == TOTAL_MORTGAGE:
            pay = self.total_amount * property_percentage_adjusted
            return pay