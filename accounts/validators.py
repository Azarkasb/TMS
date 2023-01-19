from django.core import validators

phone_validator = validators.RegexValidator(
    r"^09\d{9}$", "فرمت شماره وارد شده صحیح نیست (شماره باید با ۰۹ شروع شود)"
)
