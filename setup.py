from setuptools import find_packages, setup

setup(name='posterr',
      version='1.0.0',
      description='posterr app',
      author='Gabriel Jesus',
      install_requires=['pymongo', 'marshmallow', 'pytest', 'Flask', 'setuptools'],
      packages=find_packages())
