from math import exp
#logistic regression
l_rate=0.09
n_epoch=11
def predict(row, coefficients):
	yhat = coefficients[0]

	for i in range(len(row)-1):
	
		yhat += coefficients[i + 1] * row[i]
	return 1.0 / (1.0 + exp(-yhat))   
    

# Estimate logistic regression coefficients using stochastic gradient descent

def coefficients_sgd(train, l_rate, n_epoch):
	global coef
	coef=[0.0 for i in range (len(train[0]))]
	# coef = [0.0 for i in range(len(train[0]))]
	# coef=[0.0 for in range (len(train))]
    # for epoch in range(n_epoch):
	for epoch in range(n_epoch):

		for row in train:
			yhat = predict(row, coef)
			error = row[-1] - yhat
			coef[0] = coef[0] + l_rate * error * yhat * (1.0 - yhat)
			for i in range(len(row)-1):
				coef[i + 1] = coef[i + 1] + l_rate * error * yhat * (1.0 - yhat) * row[i]
	return coef
 

def logistic_regression(train, test):
	print ('hello')
	coef=coefficients_sgd(train,l_rate,n_epoch)
    # coef=coefficients_sgd(train, l_rate, n_epoch)
	predictions=list()
    # predictions=list()
	for row in test:
    # for row in test:
        # yhat=predict(row,coef)
		yhat=predict(row,coef)
        # yhat=round(yhat)
		yhat=round(yhat)
        # predictions.append(yhat)
		predictions.append(yhat)
	return predictions
    # return (predictions)

def logistic_regressionoutput(aa):
	predicted=predict(aa,coef)
	print('logistic_reg')
	print(predicted)
	return predicted
