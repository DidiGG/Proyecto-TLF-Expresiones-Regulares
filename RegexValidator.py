# modelo.py

import re

class RegexValidator:
    def __init__(self, regex):
        self.regex = regex
    
    def validate(self, strings):
        try:
            pattern = re.compile(self.regex)
            results = {string: bool(pattern.fullmatch(string)) for string in strings if string.strip()}
            return results
        except re.error as e:
            raise ValueError(f"Expresión regular inválida: {e}")
