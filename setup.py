from setuptools import setup

version = "0.0.1"

setup(
    name="django-language-autoswitcher",
    version=version,
    keywords="django-language-autoswitcher",
    description="Switch language by mood",
    long_description=open('README.md').read(),
    url="",
    author="Oukanina",
    author_email="guo.ke.ke.a@gmail.com",
    package=["language_autoswitcher"],
    py_modules=[],
    install_requires=["django"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
    ],
)
