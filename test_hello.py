from hello import toyou, add, subtract


def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10


def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x


### Revise typo in on-purpose failed test
def test_hello_add():
    assert add(test_hello_add.x) == 11

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
    
if __name__ == "__main__":
    print("This is Demo Test for test.py')
    setup_function(add)
    test_hello_add()
    setup_function(subtract)
    test_hello_subtract()
