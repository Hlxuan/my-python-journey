# 背景：你要为新款“智能温控风扇”编写一个基础信息录入程序。目前程序只需把各项参数定义为对应类型的变量，并将档案信息打印出来。

# 要求：请在`exercises/basics.py`文件中编写代码，完成以下任务：

# 1. 定义产品名称：变量名为`product_name`，值为字符串“智能温控风扇 Pro Max”。
product_name = "智能温控风扇 Pro Max"

# 2. 定义产品定价：变量名为`price`，值为浮点数`299.9`。
price = 299.9

# 3. 定义库存数量：变量名为`stock`，值为整数`1500`。
stock = 1500

# 4. 定义是否支持联网：变量名为`is_smart`，值为布尔值`True`。
is_smart = True

# 5. 定义赠品信息：变量名为`free_gift`，值为空值`None`（表示暂未确定赠品）。
free_gift = None

# 6. 定义保修天数：变量名为`warranty_days`，值为整数`365`。
warranty_days = 365

# 7. 打印档案：使用`print()`函数将上述变量逐行打印出来，格式需清晰。
print("产品名称：", product_name)
print("产品定价：", price)
print("库存数量：", stock)
print("是否支持联网：", is_smart)
print("赠品信息：", free_gift)
print("保修天数：", warranty_days)

# 8. 类型核对：最后使用`type()`函数分别打印出`price`和`is_smart`这两个变量的类型，确认它们确实是`float`和`bool`。
print("price的类型：", type(price))
print("is_smart的类型：", type(is_smart))