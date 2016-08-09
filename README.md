# easybook
证券多账户账户、多策略的下单管理

- 主要对 easytrader 提供支持
- 也许会对Python2提供支持

## 环境配置
anaconda3-2.5.0(建议) or Python3.5+ or Python2.7+

```python
import easybook
# 配置账户初始信息
easybook.accounts_path = "tmp/accounts.json"
# 创建全局唯一的账本实例
book = easybook.get_book()
```

账簿有记账和下单两个模块
记账模块，打算用复式记账，sqlachamy 来保存
下单模块，有个队列，下单的时候往队列里面提交
并且下单是加减仓模式的
比如我现在500股万科A，要加仓到 700股，那么提交给账簿的订单就是 也是这样子的，如果策略触发了多次提交，那么第一次成功下单之后
在处理重复提交的第二个订单，会发现万科A已经是700股了，不符合 500股增仓到 700 这个操作，就会作废