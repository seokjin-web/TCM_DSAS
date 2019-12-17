#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:46  2019/12/9
#@Author  :    tb_youth
#@FileName:    Lasso.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth



from sklearn import linear_model
import pandas as pd
import os
import numpy as np
import math


'''
  Lasso的全称叫做Least absolute shrinkage and selection operator，
  直译过来为最小收缩与选择算子。
  其本质就是在常规的线性回归的基础上对参数加了一个L1正则化约束。
'''
class LassoDemo():
    def __init__(self,df,var_list,parameter_dict):
        self.df = df
        self.x_labels = self.df.columns.values
        self.x_data = self.df[var_list[0]]
        self.y_data = self.df[var_list[1][0]]
        self.lasso_model = linear_model.Lasso(alpha=parameter_dict.get('alpha'), max_iter=parameter_dict.get('max_iter'))
        self.best_features = []
    
    def run(self):
        
        self.lasso_model.fit(self.x_data, self.y_data)

        # 权重系数，为0则代表该特征剔除
        # print(self.lasso_model.coef_)
        coef = pd.Series(self.lasso_model.coef_)

        # 留下的特征数目
        print('选出的特征共{}个:'.format(sum(coef != 0)))

        # 保存留下的特征
        for i, item in enumerate(coef):
            if item != 0:
                feature = self.x_labels[i]
                self.best_features.append(feature)
                print(feature)
        return self.best_features
    
    def analysis(self):
        # 预测
        self.y_old_predict = [self.lasso_model.predict(self.x_data.values[i, np.newaxis])[0] for i in
                              range(len(self.x_data.values))]
        # print(self.old_predcit)
        self.now_x_data = self.df[self.best_features]
        # print(self.now_x_data)
        self.lasso_model.fit(self.now_x_data, self.y_data)
        self.y_now_predict = [self.lasso_model.predict(self.now_x_data.values[i, np.newaxis])[0] for i in
                            range(len(self.now_x_data.values))]
        now_RMSE = get_RMSE(self.y_now_predict, self.y_data.values)
        old_RMSE = get_RMSE(self.y_old_predict, self.y_data.values)
        print('old_RMSE:{},now_RMSE:{}'.format(old_RMSE,now_RMSE ))
        RMSE = old_RMSE,now_RMSE

        compare = pd.DataFrame()
        compare['y'] = self.y_data.values
        compare['y_old_predict'] =  self.y_old_predict
        compare['y_now_predict'] = self.y_now_predict
        print(compare)
        return RMSE,compare


# RMSE：均方根误差，越小越好
def get_RMSE(y_predict, y_test):
    MSE = np.mean((y_test - y_predict) ** 2)
    RMSE = math.sqrt(MSE)
    return RMSE

    
if __name__=='__main__':
    # print(os.getcwd())
    os.chdir('..')
    # print(os.getcwd())
    # print(os.path.abspath('.'))
    path = r'./data/data2.xlsx'
    df = pd.read_excel(path,index_col=0)
    parameter_dict = {
        'alpha':50,
        'max_iter':20000,
    }
    header_list = df.columns.values.tolist()
    var_list = [header_list[:-1], [header_list[-1]]]
    lasso = LassoDemo(df,var_list,parameter_dict)
    lasso.run()
    lasso.analysis()



