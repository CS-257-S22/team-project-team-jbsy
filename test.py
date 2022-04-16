import unittest
import project

class TestSOMETHING(unittest.TestCase):
    def test_approval(self):
        self.assertEqual(project.getCompaniesByState("SD"),"NATIONAL MUSIC MUSEUM");
       # self.assertEqual(test("0 NORTH AVE WAKEFIELD LLC"),"1");
    #def test_denial(self):
       # self.assertEqual(test("7CINFO COM INC"),"1");
       # self.assertEqual(test("ACORNS GROW INCORPORATED"),"0");
if __name__ == '__main__':
      print(project.getCompaniesByState("SD"));
      unittest.main()
