# ### 1. 温度判断
# 使用`input()`函数获取用户输入的温度（需转换为浮点数）。
# - 如果温度>= 30，打印“高温模式：风扇最大转速”。
# - 如果温度在20到29之间，打印“舒适模式：风扇中速运转”。
# - 如果温度在10到19之间，打印“凉爽模式：风扇低速运转”。
# - 如果温度<10，打印“寒冷模式：风扇关闭”。

temperature = float(input("请输入温度："))

if temperature >= 30:
    print("高温模式：风扇最大转速")
elif temperature >= 20:
    print("舒适模式：风扇中速运转")
elif temperature >= 10:
    print("凉爽模式：风扇低速运转")
else:
    print("寒冷模式：风扇关闭")

# ### 2. 倒计时启动
# 风扇启动前需要有3秒倒计时。使用`while`或`for`循环配合`range()`打印“3, 2, 1, 启动！”。

if temperature >= 10:
    for i in range(3, 0, -1):
        print(i, end=", ")
    print("启动！")


# ### 3. 传感器模拟
# 假设有5个温度传感器，温度值分别为 [28, 32, 25, 18, 35]。使用`for`循环遍历，如果检测到温度>=30，打印警告“警告：传感器X温度过高！”，并使用`continue`跳过后续处理；如果温度正常，打印“传感器X正常”。如果所有传感器都正常，尝试使用`for...else`结构打印“所有传感器均正常”。

all_normal = True
temps = [28, 32, 25, 18, 35]
for index, temp in enumerate(temps):
    if temperature >= 30 and temp >= temperature:
        print(f"警告：传感器{index+1}温度过高！")
        all_normal = False
        continue
    print(f"传感器{index+1}正常")
else:
    if all_normal:
        print("所有传感器均正常")
