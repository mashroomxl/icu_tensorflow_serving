# Update the code and upload the package to pypi
# 1. python ./setup.py sdist --format=gztar
# 2. twine upload dist/simple_tensorflow_serving-1.0.0.tar.gz

try:
  from setuptools import setup
  setup()
except ImportError:
  from distutils.core import setup

setup(
    name="simple_tensorflow_serving",
    version="0.1",
    author="icm",
    author_email="mashroomxl@gmail.com",
    url="https://github.com/mashroomxl/icu_tensorflow_serving",
    install_requires=["tensorflow>=1.7.0"],
    description="an easy-to-use serving service for TensorFlow models",
    packages=[
        "simple_tensorflow_serving",
        "simple_tensorflow_serving.gen_client",
        "simple_tensorflow_serving.conf",
        "simple_tensorflow_serving.sources",
        "simple_tensorflow_serving.static",
        "simple_tensorflow_serving.templates"
    ],
    package_data={'templates': ['*'], 'static': ['*']},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "simple_tensorflow_serving=simple_tensorflow_serving.server:main",
        ],
    })
