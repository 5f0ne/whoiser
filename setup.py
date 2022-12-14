from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="whoiser",
    version="1.0.0",
    author="5f0",
    url="https://github.com/5f0ne/whoiser",
    description="whois information for given IP addresses",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    install_requires=[
        "ipwhois"
    ],
     entry_points={
        "console_scripts": [
            "whoiser = whoiser.__main__:main"
        ]
    }
)
