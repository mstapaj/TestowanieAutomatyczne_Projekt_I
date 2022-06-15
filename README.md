## School Diary Project

Project of a school diary where you can add, edit, delete students, subjects, grades, remarks, with the ability to import/export the data to a CSV file. The project was made for a Automated Testing course at the University of Gdańsk.

## Project Status

Project completed on 8 December 2021

[![CI](https://github.com/mstapaj/TestowanieAutomatyczne_Projekt_I/actions/workflows/tests.yml/badge.svg)](https://github.com/mstapaj/TestowanieAutomatyczne_Projekt_I/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/mstapaj/TestowanieAutomatyczne_Projekt_I/branch/main/graph/badge.svg?token=M8STI1TDIU)](https://codecov.io/gh/mstapaj/TestowanieAutomatyczne_Projekt_I)

## Technologies Used

- assertpy
- codecov
- coverage
- csv
- DocTest
- nose2
- parameterized
- PyHamcrest
- pytest

## Installation and Setup Instructions

#### Example:

Clone down this repository.

Installation:

`pip install -r requirements.txt`

To Run Test Suite:

`python setup.py test` or `nose2`

To Run Test Suite with Coverage:

`nose2 --with-coverage`

## Functionalities

- It is possible to add, edit, delete students, subjects, grades, remarks.
- You can show information about students, subjects, grades, remarks.
- You can view a student's grade average and a student's grade average for a given subject.
- It is possible to import/export all data to CSV file.
- The test libraries assertpy, PyHamcrest and pytest were used. Various types of assertions (including custom matchers)
  were used in the tests.
- Parametric tests from the parameterized library have been added to the project.
- CI is added to the project using the Codecov website.
- The TDD methodology was used.
