import pytest

print "=== 1 ===="

@pytest.fixture(scope='function')
def setup_function(request):
    print "define setup_function"
    def teardown_function():
        print("teardown_function called.")
    request.addfinalizer(teardown_function)
    print('setup_function called.')

print "=== 2 ===="

@pytest.fixture(scope='module')
def setup_module(request):
    print "define setup_moudle"
    def teardown_module():
        print("teardown_module called.")
    request.addfinalizer(teardown_module)
    print('setup_module called.')

print "=== 3 ===="

def test_1(setup_function):
    print('Test_1 called.')

print "=== 4 ===="
def test_2(setup_module):
    print('Test_2 called.')

print "=== 5 ===="
def test_3(setup_module):
    print('Test_3 called.')
