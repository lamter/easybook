# coding=utf8
import json
import os
import logging
from collections import OrderedDict

import arrow

from .account import Account


class Book:
    """
    唯一的账本实例
    """

    def __init__(self, accounts_path):
        self.accounts_path = accounts_path
        self.log = logging.getLogger("book")
        self.traders = {}
        self.accounts = {}

    def new_trader(self, **traders):
        """
        添加交易交口的实例,目前仅支持 easytrader
        :param traders: {"trader_name": trader}
        :return:
        """
        for n, t in traders.items():
            if n in self.traders:
                err = "已经存在交易接口 %s" % n
                self.log.error(err)
                raise ValueError()
            self.traders[n] = traders

    def load_accounts(self, path=None):
        """
        :param path: 账户的信息
        :return:
        """
        path = path or self.accounts_path
        with open(path, 'r') as f:
            dic = json.load(f)

        for a, info in dic.items():
            a = Account.load(info)
            if a.name in self.accounts:
                err = "已经存在账户%s" % a.name
                self.log.error(err)
                raise TypeError(err)
            # 加载成功
            self.accounts[a.name] = a

    def save_accounts(self):
        """
        :return:
        """
        if not self.accounts:
            self.log.debug("没有需要保存的账号信息")
            return

        accounts = {}
        for a in self.accounts.values():
            accounts[a.name] = a.to_save()

        # 如果已经存在账户信息文件了,那么改名,重新保存
        if os.path.exists(self.accounts_path):
            ctime = arrow.get(os.path.getctime(self.accounts_path))
            old_name = self.accounts_path.split(".json")[0]
            new_name = old_name + ctime.format(" YYYY-MM-DD HH:mm:ss") + '.json'
            os.rename(self.accounts_path, new_name)

        # 保存
        with open(self.accounts_path, 'w') as f:
            json.dump(accounts, f, indent=4)


    def get_traders(self, traders):
        """
        :return:
        """
        ordic = OrderedDict()
        for t in traders:
            trader = self.traders.get(t)
            if trader is None:
                self.log.warn("未知的交易接口 %s" % t)
                continue

            ordic[t] = trader
        return ordic

    def alltraders(self):
        return OrderedDict(self.traders)
