# coding=utf8

import pandas as pd
import sqlalchemy

class Account:
    """
    账户类,在账本上注册账户
    """

    STOCKS_COLUMNS = ["stock_code", "stock_name", "current_amount", "enable_amount"]

    def __init__(self, book):
        self.book = book
        self.name = ""
        self.path = ""
        # 可以使用的交易账户,有优先级
        self._traders = []

        # 账户数据
        self.enable_balance = 0  # 可用资金
        self.stocks = pd.DataFrame(columns=self.STOCKS_COLUMNS)  # 股票持仓

    @property
    def log(self):
        return self.log

    @property
    def traders(self):
        if self._traders:
            return self.book.get_traders(self._traders)
        else:
            return self.book.alltraders()

    @classmethod
    def load(cls, dic):
        """

        :param dic:
        :return:
        """
        name = dic.get("name")
        if name is None:
            raise ValueError("账户的名称丢失")

        account = cls()

        dic.pop("stocks")

        for k, v in dic.items():
            if not hasattr(account, k):
                raise ValueError("数据 %s 尚未定义" % k)
            setattr(account, k, v)

        return account

    def to_save(self):
        return {k: v for k, v in self.__dict__.items() if k != 'book'}
