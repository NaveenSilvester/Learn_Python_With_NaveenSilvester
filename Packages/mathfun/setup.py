from setuptools import setup, find_packages

setup(
    name = "mathfun", # Package Name
    version = "1.0.0" # Version
    author = "Naveen Silvester",
    author_email = "silvester.naveen@gmail.com",
    description = "A simple math utilities package",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    url="https://github.com/NaveenSilvester/Learn_Python_With_NaveenSilvester/Pacakages/mathfun", # Github repo
    packages =find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent", 
        ],
    python_requires = ">=3.6",
)
