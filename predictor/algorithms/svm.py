import numpy as np
import pandas as pd
from sklearn.svm import SVC
# numpy_array= np.array(h)
# df= pd.DataFrame(numpy_array, columns=['Age','Gender','Polyuria', 'Polydipsia','sudden weight loss', 'weakness','Polyphagia','Gential thrush', 'visual blurring', 'Irritability', 'partial paresis', 'muscle stiffness', 'Alopecia','class'])
# print(df.head(5))
# q=df.to_numpy()
# print(q)


def svmalgorithm(train_set1, test_set1):
    global svmclassifier
    train=np.array(train_set1)
    train_set=pd.DataFrame(train, columns=['Age','Gender','Polyuria', 'Polydipsia','sudden weight loss', 'weakness','Polyphagia','Gential thrush', 'visual blurring', 'Irritability', 'partial paresis', 'muscle stiffness', 'Alopecia','class'])
    test=np.array(test_set1)
    test_set=pd.DataFrame(test, columns=['Age','Gender','Polyuria', 'Polydipsia','sudden weight loss', 'weakness','Polyphagia','Gential thrush', 'visual blurring', 'Irritability', 'partial paresis', 'muscle stiffness', 'Alopecia','class'])
    X_train=train_set.drop('class', axis=1)
    y_train= train_set['class']
    X_test=test_set.drop('class', axis=1)
    y_test= test_set['class']
    svmclassifier= SVC(kernel='linear')
    svmclassifier.fit(X_train, y_train)
    y= svmclassifier.predict(X_test)
    print('sabin')
 
    return y

def svmalgorithmoutput(bb):
    pre1=pd.DataFrame({'Age':[bb[0][0]],'Gender':[bb[0][1]],'Polyuria':[bb[0][2]],'Polydipsia':[bb[0][3]],'sudden weight loss':[bb[0][4]],'weakness':[bb[0][5]],'Polyphagia':[bb[0][6]],'Gential thrush':[bb[0][7]],'visual blurring':[bb[0][8]],'Irritability':[bb[0][9]],'partial paresis':[bb[0][10]],'muscle stiffness':[bb[0][11]],
    'Alopecia':[bb[0][12]]})

    xxx=svmclassifier.predict(pre1)
    return (xxx)
   

