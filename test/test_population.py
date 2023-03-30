import pytest
from main import fileRead
from main import printPopulation

def test_fileRead():
    # create a test file with some data
    with open('test_data.txt', 'w') as file:
        file.write("USA, 2020, 330000000\n")
        file.write("USA, 2021, 335000000\n")
        file.write("India, 2020, 1380000000\n")
        file.write("India, 2021, 1390000000\n")

    # call the fileRead() function with the test file
    country_populations = fileRead('test_data.txt')

    # check if the output is as expected
    assert country_populations == {
        'USA': [('2020', 330000000), ('2021', 335000000)],
        'India': [('2020', 1380000000), ('2021', 1390000000)]
    }

@pytest.fixture
def country_populations():
    return {
        'USA': [('2020', 330000000), ('2021', 335000000)],
        'India': [('2020', 1380000000), ('2021', 1390000000)]
    }

def test_printPopulation(capfd, country_populations):
    printPopulation(country_populations)
    out, err = capfd.readouterr()
    assert out == "USA:\n2020 -> 2021: 5000000\nIndia:\n2020 -> 2021: 10000000\n"



