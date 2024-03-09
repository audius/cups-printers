"""Setup file for CUPS printers."""
import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='cups_printers',
    version='0.2.0',
    description='Get the printers from a running CUPS instance.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/audiusGmbH/cups_printers',
    download_url='https://github.com/audiusGmbH/cups_printers/releases',
    author='Fabian Affolter',
    author_email='fabian.affolter@audius.de',
    license='MIT',
    install_requires=['pycups', 'click'],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'cups_printers = cups_printers.cli:cli'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Utilities',
    ],
)
