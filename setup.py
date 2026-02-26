
from setuptools import find_packages, setup

setup(
    name='pricing_engine',
    version='0.0.1',
    author='Songram Biswas',
    author_email='songrambiswas359@gmail.com',
    # This tells Python that the code starts inside the 'src' folder
    package_dir={"": "src"}, 
    packages=find_packages(where="src"),
    install_requires=[]
)