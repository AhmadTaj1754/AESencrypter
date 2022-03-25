import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="AESencrypt",
    version="0.0.5",
    author="Ahmad Taj",
    author_email="Ahmadtaj77@gmail.com",
    description="tool for encrypting files using AES encryption",
    long_description="""AESencrypter is a cross-platform file encryption Python mini-app which can be accessed via The Python Package Index (PyPI).

Install AESencrypter on your system using :

pip3 install AESencrypt

Import AESencrypter into your project using :

import AESencrypter

Example of creating and using instance of AESencrypter:

import AESencrypter

AESencrypter.create()

*works best with Python3""",
    long_description_content_type="text/markdown",
    url="https://github.com/AhmadTaj1754/AESencrypter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
