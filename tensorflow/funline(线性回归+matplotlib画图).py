# 线性函数实现f(x)=x*W+b
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

# 创建数据
x_data = np.random.rand(100).astype(np.float32)

# 计算公式
y_data = x_data * 8 + 1.8

# 设置权重W b
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

# 预测Y值
y = x_data * Weights + biases 

# 预测值和目标值差值
loss = tf.reduce_mean(tf.square(y-y_data))

# 梯度下降 学习率如何确定
# 梯度下降优化
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 0.5 学习率
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for step in range(201):
        sess.run(train)
        if step % 20 == 0 :
            print("step={}\tWerghts={}\tBiases={}".format(step,sess.run(Weights),sess.run(biases)))
            # print(sess.run(y))
            # print(step,sess.run(Weights),sess.run(biases))
            # 画图显示出图像
            # plt.plot(x_data, sess.run(y))

    plt.plot(x_data, sess.run(y))
# print(y.shape)
plt.show()
#     print(sess.run(y))

# print(x_data)
# print(y_data)


