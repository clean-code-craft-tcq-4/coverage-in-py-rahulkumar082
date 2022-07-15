import unittest
from breach.check_and_alert import Check_and_Alert

test_obj = Check_and_Alert()

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(test_obj.typewise_alert('PASSIVE', 'TO_CONTROLLER', 'rahul', ['temperature'], [25]) == '65261, NORMAL')


if __name__ == '__main__':
  unittest.main()
