from my_project.weather import check_weather
# passed
def not_a_test_check_weather1():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
    must be considered as hot'

# failed
def test_check_weather2():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
        must be considered as average temperature'

# passed
def test_check_weather3():
    assert check_weather(5.00) == "cold", 'temperatures lower than 10 degree must be considered as cold'

# failed
def test_check_weather4():
    assert check_weather(13.00) == "average", 'temperatures between 10 and 20 degree \
        must be considered as average temperature'

