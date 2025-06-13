from setuptools import setup, find_packages

setup(
    name="4us-app",
    version="0.1",
    packages=find_packages(where="backend"),
    package_dir={"": "backend"},
)
