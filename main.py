import unittest
import numpy as np
''' compute the median of an array'''
array = [1, 2, 5, 4, 6, 7, 3]


def Median(array):
    '''
    Input an array and return the median number of the array
    Args:
        array: an array with n numbers
    Returns:
        array[m_index]: the median nubmer
            m_index: the index of the median number in array
    '''
    n = len(array)
    m_index = n // 2
    array = sorted(array)
    return array[m_index]


class TestMethods(unittest.TestCase):
    ''' unittest '''

    def test_median(self):
        self.assertEqual(m, M)


''' test for the entire method '''
m = Median(array)
M = np.median(array)
print(m)

if __name__ == '__main__':
    unittest.main()
