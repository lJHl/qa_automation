# -*- coding: utf-8 -*-
from db.db_worker import DBWorker
from db.sql_requests import SQLRequests
from utils.config_parser import ConfigParser
from utils.settings_parser import SettingsParser
import logging


if __name__ == "__main__":

    config = ConfigParser().get_config_settings()
    settings = SettingsParser().get_test_settings()

    logging.basicConfig(filename=config['log_filename'], level=logging.INFO, format=config['log_format'])
    logger = logging.getLogger()

    db_worker = DBWorker(config['host'], config['user'], config['password'], config['database'])
    sql_request = SQLRequests(db_worker, settings)

    try:
        db_worker.connect()

        logger.info('Шаг 1')

        sql_request.get_min_working_time()

        logger.info('-' * 200)

        logger.info('Шаг 2')

        sql_request.get_count_all_project()

        logger.info('-' * 200)

        # Step 3

        logger.info('Шаг 3')

        sql_request.get_tests_with_specific_date(settings['date'])

        logger.info('-' * 200)

        # Step 4

        logger.info('Шаг 4')

        sql_request.get_tests_by_browser(settings['browser_one'], settings['browser_two'])

    except:
        logger.error("Database is not open")
    finally:
        db_worker.disconnect()
