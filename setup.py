import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="AESencrypt",
    version="0.0.5",
    author="Ahmad Taj",
    author_email="Ahmadtaj77@gmail.com",
    description="tool for encrypting files using AES encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AhmadTaj1754/AESencrypter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
