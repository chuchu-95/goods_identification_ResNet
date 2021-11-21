基本功能：
对零售商品数据集进行处理，然后进行模型训练，生成预测模型，对图片进行预测分类

代码运行：
	运行环境为华为云ModelArts,Notebook, 将src目录中代码按顺序导入JupyterLab；
	运行成功后，train.py文件作为训练脚本文件，输出训练次数以及对应的损失率，eval作为评估脚本，输出准确率，预测结果和真实结果。


目录结构：

├── goodsCode
   	├── README.md                    // 代码架构相关说明
    ├── src
	│   ├── config.py  				//定义变量
	│   ├── dataset.py             // 数据集处理函数
	│   ├── resnet.py   				//resNet架构
	│   ├── define_dynamic_study.py    //自定义动态学习率
    ├── train.py              			// 训练脚本
	├── eval.py              			// 评估脚本
    ├── preprocessing_dataset.py         //预处理脚本（解压文件夹）