from distutils.core import setup

setup(
    name='rabbitmq_asynqp',
    version='0.1.0',
    author='Akshay Agarwal',
    author_email='akshay2agarwal@gmail.com',
    packages=['rabbitmq_asynqp'],
    scripts=['bin/example.py'],
    url='http://pypi.python.org/pypi/rabbitmq_asynqp/',
    license='LICENSE.txt',
    description='Implementation of rabbitmq with asynqp',
    long_description=open('README.txt').read(),
    install_requires=[
        "asynqp >= 0.5.1"
    ],
)
