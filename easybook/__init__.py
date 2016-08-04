# coding=utf8

setting_paht = "setting.json"
accounts_path = "tmp/account.json"

from . import book
from .api import *

mybook = None


def get_book():
    """
    获得唯一的账本实例
    :return:
    """
    global mybook
    if mybook is None:
        mybook = book.Book(accounts_path)
    return mybook
