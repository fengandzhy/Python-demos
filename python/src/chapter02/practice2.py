"""
实战与练习

2. 现在有一个变量x，值为5423.5346，使用format函数对该变量进行格式化，并使用print函数输出如下的5个格式化后的值。
（1）保留小数点后3位数字，格式化后的结果：5423.535。
（2）保留小数点后2位数字，让整数和小数部分，以及小数点一共占10位，左侧位数不够补0。格式化后的结果：0005423.53。
（3）保留小数点后2位数字，让整数和小数部分，以及小数点一共占10位，右侧位数不够补0。格式化后的结果：5423.53000。
（4）在第2个格式化结果的基础上，在千分位用逗号（,）分隔，格式化后的结果：005,423.53。
（5）保留小数点后2位数字，让整数和小数部分，以及小数点一共占10位，位数不够前后补0，格式化后的结果：05,423.530。

"""

x=5423.5346
print(format(x,'0.3f'))
print(format(x,'0>10.2f'))
print(format(x,'0<10.2f'))
print(format(x,'0>10,.2f'))
print(format(x, '0^10,.2f'))


