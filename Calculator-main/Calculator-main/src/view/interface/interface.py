from src.model.calculator import Calculator

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup



class CalculatorLayout(BoxLayout):
    def calculate(self):
        try:
            # Recolectar y validar datos de entrada
            total_amount = self.get_int_input('total_amount_input', 'Monto total')
            age = self.get_int_input('age_input', 'Edad')
            life_expectancy = self.get_int_input('life_expectancy_input', 'Esperanza de vida')
            payment_period = self.get_int_input('payment_period_input', 'Período de pago')
            property_percentage = self.get_float_input('property_percentage_input', 'Porcentaje de la propiedad')
            mortgage_type = self.get_mortgage_type()

            # Realizar cálculo
            calculator = Calculator(total_amount, age, life_expectancy, payment_period, property_percentage, mortgage_type)
            monthly_fee = calculator.calculate_monthly_fee()

            # Mostrar resultado
            self.show_popup('Resultado', f'Cuota Mensual: {monthly_fee:.2f}')
        except ValueError as e:
            self.show_popup('Error', str(e))
        except Exception as e:
            self.show_popup('Error', 'Ha ocurrido un error inesperado. Por favor, inténtelo de nuevo.')

    def get_int_input(self, widget_id, field_name):
        text = self.ids[widget_id].text
        if not text:
            raise ValueError(f'El campo "{field_name}" no puede estar vacío.')
        return int(text)

    def get_float_input(self, widget_id, field_name):
        text = self.ids[widget_id].text
        if not text:
            raise ValueError(f'El campo "{field_name}" no puede estar vacío.')
        return float(text)

    def get_mortgage_type(self):
        text = self.ids.mortgage_type_spinner.text
        if not text:
            raise ValueError('Debe seleccionar un tipo de hipoteca.')
        try:
            return self.ids.mortgage_type_spinner.values.index(text) + 1
        except ValueError:
            raise ValueError('Tipo de hipoteca no válido.')

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
