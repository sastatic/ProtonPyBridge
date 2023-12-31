import sys
proton_dir = 'external/proton-python-client'
from setuptools import setup, find_packages
from proton.constants import VERSION

setup(
    name='protonpybridge',
    version='0.1.0',
    description='A Python bridge for interacting with ProtonMail using Proton Python Client.',
    author='Sarwar ALi',
    author_email='sastatic@proton.me',
    url='https://github.com/yourusername/protonpybridge',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'proton-python-client>='+VERSION,
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'protonpybridge=protonpybridge.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)


