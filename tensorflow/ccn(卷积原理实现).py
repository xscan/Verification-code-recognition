# 卷积函数实现 TensorFlow

import tensorflow as tf
k = tf.constant([
    [1, 0, 1],
    [2, 1, 0],
    [0, 0, 1]
], dtype=tf.float32, name='k')
i = tf.constant([
    [4, 3, 1, 0],
    [2, 1, 0, 1],
    [1, 2, 4, 1],
    [3, 1, 0, 2]
], dtype=tf.float32, name='i')

# 转换卷积核
kernel = tf.reshape(k, [3, 3, 1, 1], name='kernel')
# 转换输入图像
image  = tf.reshape(i, [1, 4, 4, 1], name='image')
# 卷积加权
res = tf.squeeze(tf.nn.conv2d(image, kernel, [1, 1, 1, 1], "VALID"))

# 卷积
pp= tf.nn.conv2d(image, kernel, [1, 1, 1, 1], "VALID")


# VALID means no padding
with tf.Session() as sess:

    print ('kernel=',sess.run(kernel).shape)  
    print ("k=",sess.run(k).shape)
    print ('image=',sess.run(image))
    print ('i=',sess.run(i).shape)
    print ("ccn=",sess.run(res))
    # print (sess.run(pp))
    
    
    # print('pp=',sess.run(pp))
    # print('pp=',sess.run(pp).shape)
    # print ('res=',sess.run(res))