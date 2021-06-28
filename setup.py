from setuptools import setup, find_packages

PROJECT_NAME = 'fizzbuzz'
VERSION = '0.0.1'

config = dict(
    description='Interview Use Case',
    author='Equipmentshare Inc',
    version=VERSION,
    packages=find_packages(exclude=['tests']),
    name=PROJECT_NAME,
    tests_require=[
        'pytest'
    ]
)

if __name__ == '__main__':
    setup(**config)
