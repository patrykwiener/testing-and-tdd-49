class TestSample:

    def setup_method(self) -> None:
        print('\nIt\'s me setup_method()')

    def teardown_method(self) -> None:
        print('It\'s me teardown_method()')

    def test_sample1(self):
        print('\nTesting 1')

    def test_sample2(self):
        print('\nTesting 2')

    def test_sample3(self):
        print('\nTesting 3')
