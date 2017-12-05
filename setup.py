from setuptools import setup, find_packages

install_requires = [
]

setup_requires = [
    'pytest-runner'
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
    url="https://www.github.com/jawshua",
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    tests_require=test_requires,
    setup_requires=setup_requires,
)
