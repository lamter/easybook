# coding=utf8
import pandas as pd
import easytrader


class Account:
    """
    账户类,在账本上注册账户
    """

    def __init__(self, book):
        self.book = book
        self.name = ""
        self.path = ""
        # 可以使用的交易账户,有优先级
        self._traders = []

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

        for k, v in dic.items():
            if not hasattr(account, k):
                raise ValueError("数据 %s 尚未定义" % k)
            setattr(account, k, v)

        return account

    def to_save(self):
        return {k: v for k, v in self.__dict__.items() if k != 'book'}

    def enable_balance(self):
        """
        获得可用资金:人民币
        :return:
        """
        balance = 0
        for t in self.traders:
            if isinstance(t, easytrader.YHTrader):
                # easytrader 的银河接口
                balance = pd.DataFrame(t.balance).可用资金[0]
            else:
                err = "交易接口 %s"
                self.log.warn()

        return balance


