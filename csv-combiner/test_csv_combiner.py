import unittest
import subprocess


class TestCSVCombiner(unittest.TestCase):
    """class to test csv_combiner.py"""

    def test_one_file(self):
        """test one csv files passed as args"""
        result = subprocess.run(['python3', 'csv_combiner.py', './test-fixtures/accessories.csv'],
                                stdout=subprocess.PIPE, universal_newlines='\n')
        expected_output = 'email_hash,category,filename\nb9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Wallets,accessories.csv\nc2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Purses,accessories.csv\nfaaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18,Watches,accessories.csv\n5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e,Wallets,accessories.csv'
        self.assertEqual(result.stdout.strip(), expected_output,
                         "CSV file not combined correctly")

    def test_two_files(self):
        """test combination of two csv files"""
        result = subprocess.run(['python3', 'csv_combiner.py', './test-fixtures/accessories.csv',
                                './test-fixtures/clothing.csv'], stdout=subprocess.PIPE, universal_newlines='\n')
        expected_output = 'email_hash,category,filename\nb9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Wallets,accessories.csv\nc2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Purses,accessories.csv\nfaaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18,Watches,accessories.csv\n5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e,Wallets,accessories.csv\nb9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Cardigans,clothing.csv\nc2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Cardigans,clothing.csv\nfaaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18,Tanks,clothing.csv\n5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e,Tanks,clothing.csv'
        self.assertEqual(result.stdout.strip(), expected_output,
                         "CSV files not combined correctly")

    def test_three_files(self):
        """test combination of three csv files"""
        result = subprocess.run(['python3', 'csv_combiner.py', './test-fixtures/accessories.csv',
                                './test-fixtures/clothing.csv', './test-fixtures/household_cleaners.csv'], stdout=subprocess.PIPE, universal_newlines='\n')
        expected_output = 'email_hash,category,filename\nb9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Wallets,accessories.csv\nc2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Purses,accessories.csv\nfaaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18,Watches,accessories.csv\n5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e,Wallets,accessories.csv\nb9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Cardigans,clothing.csv\nc2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Cardigans,clothing.csv\nfaaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18,Tanks,clothing.csv\n5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e,Tanks,clothing.csv\nb9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Kitchen Cleaner,household_cleaners.csv\nc2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Kitchen Cleaner,household_cleaners.csv\nfaaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18,Kitchen Cleaner,household_cleaners.csv\n5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e,Bathroom Cleaner,household_cleaners.csv'
        self.assertEqual(result.stdout.strip(), expected_output,
                         "CSV files not combined correctly")

    def test_non_csv_files(self):
        """negative test to test if non-csv files are passed as args"""
        result = subprocess.run(
            ['python3', 'csv_combiner.py', 'random_file.py'], stdout=subprocess.PIPE)
        expected_output = b'random_file.py must be a csv file'
        self.assertEqual(result.stdout.strip(),
                         expected_output, "Did not error out")

    def test_no_args(self):
        """negative test to test if no files are passed as args"""
        result = subprocess.run(
            ['python3', 'csv_combiner.py'], stdout=subprocess.PIPE)
        expected_output = b'Must input csv files as arguments'
        self.assertEqual(result.stdout.strip(),
                         expected_output, "Did not error out")


if __name__ == '__main__':
    unittest.main()
