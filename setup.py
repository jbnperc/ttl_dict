from setuptools import setup, find_packages


setup(
    name='ttl_dict',
    version='0.1.0',
    author="Ben Nadler",
    tests_require=['nose'],
    test_suite="tests",
    packages=find_packages()
)
