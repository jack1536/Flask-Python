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

    def test_multiple_select(self):
        tablename = "myTable"
        select_cols = ["school_name", "midpoint.act.score"]
        filter_dict = {"is_in": {}, "is_btwn":{}}

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = "SELECT school_name, midpoint_act_score FROM myTable"

        self.assertEqual(actualSQL, expectedSQL)

    def test_btwn_one_condition(self):
        tablename = "myTable"
        select_cols = ["school_name"]
        filter_dict = {
            "is_in": {}, 
            "is_btwn":{"midpoint.act.score":{"min":28,"max":34,"inclusive":True}}
            }

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = "SELECT school_name FROM myTable WHERE midpoint_act_score BETWEEN 28 AND 34"

        self.assertEqual(actualSQL, expectedSQL)

    def test_btwn_two_conditions(self):
        tablename = "myTable"
        select_cols = ["school_name"]
        filter_dict = {
            "is_in": {}, 
            "is_btwn":{
                "latest.admissions.act_scores.midpoint.cumulative":{"min":0,"max":36,"inclusive":True},
                "latest.student.size":{"min":0,"max":50000,"inclusive":True}
            }
        }

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = "SELECT school_name FROM myTable WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 0 AND 36 AND latest_student_size BETWEEN 0 AND 50000"
        
        self.assertEqual(actualSQL, expectedSQL)

    def test_in(self):
        tablename = "myTable"
        select_cols = ["school_name"]
        filter_dict = {
            "is_in": {"school.region_id":["Mid East (DE, DC, MD, NJ, NY, PA)"]}, 
            "is_btwn":{}
            }

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = 'SELECT school_name FROM myTable WHERE school_region_id IN ("Mid East (DE, DC, MD, NJ, NY, PA)")'

        self.assertEqual(actualSQL, expectedSQL) 


    def test_btwn_and_in(self):
        tablename = "myTable"
        select_cols = ["school_name"]
        filter_dict = {
            "is_in": {"school.region_id":["Mid East (DE, DC, MD, NJ, NY, PA)"]}, 
            "is_btwn":{"midpoint.act.score":{"min":28,"max":34,"inclusive":True}}
            }

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = 'SELECT school_name FROM myTable WHERE midpoint_act_score BETWEEN 28 AND 34 AND school_region_id IN ("Mid East (DE, DC, MD, NJ, NY, PA)")'

        self.assertEqual(actualSQL, expectedSQL)

    def test_multiple_btwn_and_in(self):
        tablename = "codetran_collegedata.collegescorecard"
        select_cols = ["school_name"]
        filter_dict = {"is_in":{"school.institutional_characteristics.level":["4-year"],"singlesex.or.coed":["Single-Sex: Women","Co-Educational"]},"is_btwn":{"latest.admissions.act_scores.midpoint.cumulative":{"min":14,"max":34,"inclusive":True},"latest.student.size":{"min":0,"max":35000,"inclusive":True}}}

        actualSQL = qb.build_query(tablename, select_cols, filter_dict)
        expectedSQL = 'SELECT school_name FROM codetran_collegedata.collegescorecard WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 14 AND 34 AND latest_student_size BETWEEN 0 AND 35000 AND school_institutional_characteristics_level IN ("4-year") AND singlesex_or_coed IN ("Single-Sex: Women", "Co-Educational")'
        self.assertEqual(actualSQL, expectedSQL)

if __name__ == '__main__':
    unittest2.main()