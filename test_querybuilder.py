import unittest2
import querybuilder as qb

class TestLogStatement(unittest2.TestCase):

    def test_empty(self):
        tablename = "myTable"
        select_cols = ["school_name"]
        filter_dict = {"is_in": {}, "is_btwn":{}}

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = "SELECT school_name FROM myTable"

        self.assertEqual(actualSQL, expectedSQL)

    




if __name__ == '__main__':
    unittest2.main()