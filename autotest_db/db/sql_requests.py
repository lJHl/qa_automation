# -*- coding: utf-8 -*-


class SQLRequests:
    __MIN_WORKING_TIME_SORTED_BY_PROJECT_AND_TEST = \
        """
        SELECT project.name AS PROJECT, test.name AS TEST,    
        MIN(TIMESTAMPDIFF(second, test.start_time, test.end_time)) AS MIN_WORKING_TIME  
        FROM test  
        INNER JOIN project ON test.project_id = project.id  
        WHERE test.end_time IS NOT NULL AND NOT test.start_time = test.end_time
        GROUP BY PROJECT, TEST 
        ORDER BY PROJECT, TEST
        """

    __COUNT_ALL_PROJECTS_WITH_UNIQUE_TESTS = \
        """
        SELECT project.name AS PROJECT, COUNT(DISTINCT test.name) AS TEST_COUNT
        FROM test  
        INNER JOIN project ON test.project_id = project.id  
        GROUP BY project_id 
        """

    __TESTS_WITH_SPECIFIC_DATE_FOR_ALL_PROJECT_SORTED_BY_PROJECT_AND_TESTS = \
        """
        SELECT project.name AS PROJECT, test.name AS TEST, test.start_time AS TIME
        FROM test  
        INNER JOIN project ON test.project_id = project.id  
        WHERE test.start_time >= '{date}'
        ORDER BY PROJECT, TEST
        """

    __COUNT_TESTS_WERE_EXECUTED_BY_FIREFOX_AND_CHROME = \
        """
        SELECT COUNT(browser) AS BROWSERS FROM test  
        WHERE browser = '{browser_one}'
        UNION
        SELECT COUNT(browser) AS BROWSERS FROM test
        WHERE browser = '{browser_two}'
        """

    def __init__(self, inst, settings):
        self.settings = settings
        self.inst = inst

    def get_min_working_time(self):
        request = self.__MIN_WORKING_TIME_SORTED_BY_PROJECT_AND_TEST
        cursor = self.inst.execute_exp(request)
        self.inst.log({
                    "PROJECT": [x[0] for x in cursor],
                    "TEST": [x[1] for x in cursor],
                    "MIN_WORKING_TIME": [x[2] for x in cursor]
        })

    def get_count_all_project(self):
        request = self.__COUNT_ALL_PROJECTS_WITH_UNIQUE_TESTS
        cursor = self.inst.execute_exp(request)
        self.inst.log({
            "PROJECT": [x[0] for x in cursor],
            "TEST_COUNT": [x[1] for x in cursor]
        })

    def get_tests_with_specific_date(self, date):
        request = self.__TESTS_WITH_SPECIFIC_DATE_FOR_ALL_PROJECT_SORTED_BY_PROJECT_AND_TESTS.\
            format(date=date)
        cursor = self.inst.execute_exp(request)
        self.inst.log({
            "PROJECT": [x[0] for x in cursor],
            "TEST": [x[1] for x in cursor],
            "TIME": [x[2] for x in cursor]
        })

    def get_tests_by_browser(self, browser_one, browser_two):
        request = self.__COUNT_TESTS_WERE_EXECUTED_BY_FIREFOX_AND_CHROME.\
            format(browser_one=browser_one, browser_two=browser_two)
        cursor = self.inst.execute_exp(request)
        self.inst.log({"BROWSERS": [x[0] for x in cursor]})
