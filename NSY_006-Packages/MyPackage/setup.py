from setuptools import setup, find_packages

setup (
    name="Math",                   # Package name
    version="1.0.0",                  # Version
    author="Naveen Silvester",
    author_email="your.email@example.com",
    description="A simple math utilities package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mathfun",  # GitHub or other repository
packages=find_packages(),
classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
