# Malicious code here


from setuptools import setup, find_packages


with open("README.md", "r", encoding="UTF-8") as f:
    README = f.read()


setup(
    name="purposefully-malicious",
    version="0.0.1",
    url="https://github.com/benwoo1110/purposefully-malicious",

    author="benwoo1110",
    author_email="wben1110@gmail.com",

    packages=find_packages(),
    python_requires=">=3.6",

    description="Demonstrates what a malicious PyPI package could do to you :O",
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
