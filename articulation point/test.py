import tarjan as tj
import unittest

class Test(unittest.TestCase):
	
	def test0(self):
		self.assertEqual(tj.main('testcases/input0.txt'), [], 'should be []')

	def test1(self):
		self.assertEqual(tj.main('testcases/input1.txt'), ['2'], 'should be 2')

	def test2(self):
		self.assertEqual(sorted(tj.main('testcases/input2.txt')), ['2', '3'], 'should be 2, 3')

	def test3(self):
		self.assertEqual(sorted(tj.main('testcases/input3.txt')), ['2', '3', '4'], 'should be 2, 3, 4')

	def test4(self):
		self.assertEqual(sorted(tj.main('testcases/input4.txt')), ['2', '4'], 'should be 2, 4')

	def test5(self):
		self.assertEqual(sorted(tj.main('testcases/input5.txt')), ['3', '5'], 'should be 3, 5')

	def test6(self):
		self.assertEqual(sorted(tj.main('testcases/input6.txt')), ['3', '4'], 'should be 3, 4')

	def test7(self):
		self.assertEqual(sorted(tj.main('testcases/input7.txt')), ['5'], 'should be 5')
	
	def test8(self):
		self.assertEqual(sorted(tj.main('testcases/input8.txt')), [], 'should be []')

	def test9(self):
		self.assertEqual(sorted(tj.main('testcases/input9.txt')), [], 'should be []')

	def test10(self):
		self.assertEqual(sorted(tj.main('testcases/input10.txt')), [], 'should be []')

	def test11(self):
		self.assertEqual(sorted(tj.main('testcases/input11.txt')), [], 'should be []')

	def test12(self):
		self.assertEqual(sorted(tj.main('testcases/input12.txt')), ['5', '7'], 'should be 5, 7')

	def test13(self):
		self.assertEqual(sorted(tj.main('testcases/input13.txt')), ['4', '8'], 'should be 4, 8')

	def test14(self):
		self.assertEqual(sorted(tj.main('testcases/input14.txt')),['0', '107', '1684', '1912', '3437',\
											'348', '3980', '414', '594', '686', '698'] , 'should be 0, \
											107, 1684, 1912, 3437, 348, 3980, 414, 594, 686, 698')

	def test15(self):
		self.assertEqual(sorted(tj.main('testcases/input15.txt')), ['1000', '1001'], 'should be 1000, 1001')

if __name__ == '__main__':
	unittest.main()
