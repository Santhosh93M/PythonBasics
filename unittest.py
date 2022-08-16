import unittest
from testing import eat

class ActivityTests(unittest.TestCase):
	def  test_eat(self):
		self.assertEqual(eat("boiler",is_healthy=True),
			"have to eat good"
			)
		self.assertEqual(eat("Pizza",is_healthy=False),
			"Is bad for health"
			)
		
if __name__=="__main__":
	unittest.main()