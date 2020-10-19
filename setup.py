from setuptools import find_packages, setup
import os
import re

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def find_version(path):
    with open(path, 'r', encoding='utf-8') as source:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", source.read(),
                         re.M).group(1)


def read_long_description(path):
    with open(path, 'r', encoding='utf-8') as readme:
        return readme.read()


setup(
    name='virtualstaining',
    version=find_version('virtualstaining/__init__.py'),
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='Arontier Proprietary License',
    description='a virtual staining using deep learning',
    long_description=read_long_description('README.md'),
    long_description_content_type="text/markdown",
    url='https://github.com/arontier/virtualstaining',
    author='Donghwan Lee',
    author_email='dhlee@arontier.co',
    zip_safe=False,
    scripts=[
        'bin/virtualstaining-testhotspot',
        'bin/virtualstaining-testwsi',
    ],
    setup_requires=[],
    install_requires=[
        'numpy == 1.17.4',
        'matplotlib == 3.1.1',
        'opencv-python == 4.1.2.30',
        'openslide-python == 1.1.2',
        'pandas == 1.1.3',
        'scikit-image == 0.15.0',
        'scikit-learn == 0.23.2',
        'tifffile == 2020.7.4',
        'torch == 1.5.1',
        'torchvision == 0.6.1',
        'tqdm == 4.50.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
