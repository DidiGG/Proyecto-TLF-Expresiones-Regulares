# controlador.
from modelo import RegexValidator

class RegexController:
    def __init__(self, view):
        self.view = view
    
    def validate_strings(self, regex, strings):
        validator = RegexValidator(regex)
        try:
            results = validator.validate(strings)
            self.view.show_results(results)
        except ValueError as e:
            self.view.show_error(e)
