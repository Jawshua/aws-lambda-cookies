import sys
from setuptools import setup, find_packages

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
setup_requires = ['pytest-runner'] if needs_pytest else []

install_requires = [
]

test_requires = [
    'pytest',
    'pytest-cov',
]

dev_requires = []

setup(
    name="lambdacookie",
    version="0.1.0",
    description="""Provides functions to aid in outputting multiple cookies from
                   AWS Lambda functions through API Gateway.""",
    author="Joshua Welsh",
    author_email="joshua.welsh@performancehorizon.com",
    url="https://github.com/Jawshua/aws-lambda-cookies",
    include_package_data=True,
    platforms=["any"],
    license="MIT",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    tests_require=test_requires,
    setup_requires=setup_requires,
)
