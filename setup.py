from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='TestowanieAutomatyczne_Projekt_I',
    version='2.0.0',
    description='Projekt I z przedmiotu Testowanie automatyczne. Projekt dziennika internetowego z obsługą uczniów, '
                'ocen, uwag, obliczania średniej oraz z funkcjami importu/eksportu danych',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
)
