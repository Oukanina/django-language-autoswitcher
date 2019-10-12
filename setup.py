from setuptools import setup

version = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-language-autoswitcher",
    version=version,
    keywords="django-language-autoswitcher",
    description="Switch language by wind",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oukanina/django-language-autoswitcher",
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
    ],
)
