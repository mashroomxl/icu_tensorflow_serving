# Update the code and upload the package to pypi
# 1. python ./setup.py sdist --format=gztar
# 2. twine upload dist/simple_tensorflow_serving-1.0.0.tar.gz

try:
  from setuptools import setup
  setup()
except ImportError:
  from distutils.core import setup

setup(
    name="icu_tensorflow_serving",
    version="0.1",
    author="icm",
    author_email="mashroomxl@gmail.com",
    url="https://github.com/mashroomxl/icu_tensorflow_serving",
    install_requires=["tensorflow>=1.7.0"],
    description="an easy-to-use serving service for TensorFlow models",
    packages=[
        "simple_tensorflow_serving",
        "simple_tensorflow_serving.gen_client",
        "simple_tensorflow_serving.conf"
    ],
    package_data={
        "simple_tensorflow_serving": [
            'static',
            'static/bootstrap-4.0.0-dist',
            'static/bootstrap-4.0.0-dist/*',
            'static/bootstrap-4.0.0-dist/css',
            'static/bootstrap-4.0.0-dist/js',
            'static/images',
            'static/images/*',
            'static/jquery',
            'static/jquery/*',
            'static/jquery/dist',
            'static/jquery/dist/*',
            'static/jquery/external',
            'static/jquery/external/sizzle',
            'static/jquery/external/sizzle/*',
            'static/jquery/external/sizzle/dist',
            'static/jquery/external/sizzle/dist/*',
            'static/jquery/src'
        ],
        "simple_tensorflow_serving": [
            'templates/*'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "simple_tensorflow_serving=simple_tensorflow_serving.server:main",
        ],
    })
