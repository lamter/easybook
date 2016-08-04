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