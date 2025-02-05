import re
from rest_framework.exceptions import ValidationError

def validate_passport(passport):
    if re.search(r"^[0-9]{10}$", passport) is None:
        raise ValidationError("Паспорт должен содержать 10 цифр")

def validate_snils(snils):
    if re.search(r"^[0-9]{11}$", snils) is None:
        raise ValidationError("Снилс должен содержать 11 цифр")

def validate_insurance(insurance):
    if re.search(r"^[0-9]{16}$", insurance) is None:
        raise ValidationError("Неверно введен страховой полис")