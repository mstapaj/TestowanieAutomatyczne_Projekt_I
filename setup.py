"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='TestowanieAutomatyczne_Projekt_I',
    version='2.0.0',
    description='Projekt I z przedmiotu Testowanie automatyczne. Projekt dziennika internetowego z obsługą uczniów, '
                'ocen, uwag, obliczania średniej oraz z funkcjami importu/eksportu danych',
    url='https://github.com/mstapaj/TestowanieAutomatyczne_Projekt_I',
    author='Mateusz Stapaj',
    author_email='mtxstapaj@gmail.com',
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=['parameterized',
                      'coverage',
                      'assertpy',
                      'PyHamcrest',
                      'nose2',
                      'pytest'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
