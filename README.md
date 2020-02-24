# Usage
```
pip install django-language-autoswitcher
```


```
MiDDLEWARE = (
    # ...
    'language_autoswitcher.middleware.LanguageAutoSwitcherMiddleware',
)

# Default language is English ('en')
# Keywords would be detected in URL query parameters and cookie
# If one of keywords has been detected, middleware would change the language by the value
# Priority: URL query parameters > cookie > HTTP_ACCEPT_LANGUAGE
LANGUAGES_KEY = ['lng', 'l']
```
