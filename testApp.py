from app import *
import unittest

class TestError(unittest.TestCase):
    """Test Error Page"""

    def test_404(self):
        self.app = app.test_client()
        response = self.app.get('/notExist', follow_redirects=True)
        self.assertIn(b"404 Error", response.data)
        self.assertIn(b"Page not found: the requested URL was not found.\n", response.data)

    def test_500(self):
        print("Not necessary to make test for 500 error yet")
        pass


class TestFeature(unittest.TestCase):
    """Test for Feature"""

    def test_home1(self):
        """Test the second way to access homePage: /"""

        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)

        # Check Heading
        self.assertIn(b'Welcome to H-1B Employer Data Hub!', response.data)

        # Check 1st in List
        self.assertIn(b'Get Companies By State:', response.data)

        # Check 2nd in List
        self.assertIn(b'Get Companies With Minimum Initial Approval:', response.data)
    
    def test_home2(self):
        """Test the second way to access homePage: /home"""

        self.app = app.test_client()
        response = self.app.get('/home', follow_redirects=True)

        # Check Heading
        self.assertIn(b'Welcome to H-1B Employer Data Hub!', response.data)

        # Check 1st in List
        self.assertIn(b'Get Companies By State:', response.data)

        # Check 2nd in List
        self.assertIn(b'Get Companies With Minimum Initial Approval:', response.data)
    
    def test_invalidState_listCompaniesInState(self):
        """Test for inputting invalid state"""

        self.app = app.test_client()
        response = self.app.get('/companies/search?state=1', follow_redirects=True)

        # Check error message
        self.assertIn(b'1 is not a state. Please input a valid state', response.data)

    def test_listCompaniesInState(self):
        """Test for listing companies in state"""

        self.app = app.test_client()
        response = self.app.get('/companies/search?state=AZ', follow_redirects=True)

        # Check heading
        self.assertIn(b'List of Employers in AZ for 2020:', response.data)

        # Check Body
        self.assertIn(b'Companies:', response.data)

        # Check if appropriate companies were listed
        self.assertIn(b'REDDY GI ASSOCIATES', response.data)
        self.assertIn(b'ADMIRAL INSTRUMENTS LLC', response.data)

    def test_invalidData_listCompaniesWithMinInitApproval(self):
        """Test for inputting invalid minInitApproval"""

        self.app = app.test_client()
        response = self.app.get('/companies/search?minInitApproval=hi', follow_redirects=True)

        # Check error message
        self.assertIn(b'hi is not a number. Please input a valid number!', response.data)

    def test_listCompaniesWithMinInitApproval(self):
        """Test for listing companies with minInitApproval"""

        self.app = app.test_client()
        response = self.app.get('/companies/search?minInitApproval=15', follow_redirects=True)

        # Check heading
        self.assertIn(b'List of Employers with at least 15 Minimum Initial Approval(s) for 2020:', response.data)

        # Check Body
        self.assertIn(b'Companies:', response.data)

        # Check if appropriate companies were listed
        self.assertIn(b'STATE OF CA SECY OF STATE S OFFICE', response.data)
        self.assertIn(b'EMERALD HEALTH PHARMACEUTICALS INC', response.data)


def main():
    # unittest.main(verbosity=2)
    unittest.main()

if __name__ == '__main__':
    main()
