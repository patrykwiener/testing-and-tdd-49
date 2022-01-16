def setup_module():
    print('\nHi, I\'m setup_module()')

def teardown_module():
    print('Hi, I\'m teardown_module()')

class TestSample:

    @classmethod
    def setup_class(cls):
        print('Hello here is setup_class()')

    @classmethod
    def teardown_class(cls):
        print('Hello here is teardown_class()')

    def setup_method(self):
        print('\nIt\'s me setup_method()')

    def teardown_method(self):
        print('It\'s me teardown_method()')

    def test_sample1(self):
        print('\nTesting 1')

    def test_sample2(self):
        print('\nTesting 2')

    def test_sample3(self):
        print('\nTesting 3')
