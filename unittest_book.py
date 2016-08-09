# coding=utf8
import unittest

import easybook


class TestBook(unittest.TestCase):
    def setUp(self):
        self.account_setting = "testdata/accounts.json"
        self.book = easybook.get_book()

    def test_book(self):
        self.assertIsInstance(self.book, easybook.book.Book)

    def test_create_account(self):
        """
        :return:
        """
        self.book.load_accounts(self.account_setting)

    def test_save_accounts(self):
        self.book.load_accounts(self.account_setting)

        self.account_setting = "tmp/accounts.json"
        self.book.save_accounts()

