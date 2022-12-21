import unittest

class TestUserInformation(unittest.TestCase):
    def test_user_information(self):
        # Test valid input
        with patch('builtins.input', side_effect=['John Doe', '01/01/2000', 'American', '123456789']):
            user_information()
        # Test invalid name
        with patch('builtins.input', side_effect=['John', '01/01/2000', 'American', '123456789']):
            user_information()
        # Test invalid date
        with patch('builtins.input', side_effect=['John Doe', '01/45/2022', 'American', '123456789']):
            user_information()


class TestTeachersList(unittest.TestCase):
    def test_teachers_list(self):
        # Test valid input
        with patch('builtins.input', side_effect=['Melainie', '09 AM']):
            teachers_list('Melainie')
        # Test invalid teacher
        with patch('builtins.input', side_effect=['Melain', '09 AM']):
            teachers_list('John')
        # Test invalid time
        with patch('builtins.input', side_effect=['Melainie', '09']):
            teachers_list('Melainie')

class TestPlaceOrder(unittest.TestCase):
    def test_place_order(self):
        # Test valid input
        with patch('builtins.input', side_effect=['English', 'Y']):
            placeOrder()
        # Test invalid exam
        with patch('builtins.input', side_effect=['Frnch', 'Y']):
            placeOrder()
        # Test cancel order
        with patch('builtins.input', side_effect=['English', 'N']):
            placeOrder()

if __name__ == '__main__':
    unittest.main()

