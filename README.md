# 深度学习-验证码识别例子

* 开发环境  
    * windows7_64bit 
    * python3.5.2
    * open cv


##1. 环境初始化
执行安装程序依赖的库（opencv库需手动安装或者直接下载whl文件安装）


    pip3 install -r requirements.txt

##2. 运行步骤
1. 生成测试图片(generateImage-Thread.py)
2. 图片二值化处理(step2.py)
3. 图片分割为单个字符(step3.py)
4. 图片大小统一调整(step4.py)
5. 通过tensorflow+keras训练模型(step5.py)
6. 测试模型(step_last.py)

##3. 模型应用
直接执行`step_last.py`文件即可从`test_img`文件夹中取得识别图片进行识别

model_labels.dat(标签序列化文件)
captcha_model.hdf5(特征值文件)


