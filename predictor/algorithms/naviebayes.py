#split the dataset by class value , return a dictionary
from math import sqrt
from math import exp
from math import pi
 

def separate_by_class(train_set):
    seperated=dict()
  
    for i in range(len(train_set)):
        vector=train_set[i]
        class_value=vector[-1]
        if (class_value not in seperated):
           
            seperated[class_value]=list()
        seperated[class_value].append(vector)
    return seperated


#calculate the mean of a list of numbers
def mean(numbers):
    return sum(numbers)/float(len(numbers))

#calculate the standard deviation of a list of number 
def stdev(numbers):
    avg=mean(numbers)
    variance=sum([(x-avg)**2 for x in numbers])/float(len(numbers)-1)
    return sqrt(variance)
#calculate the mean, stdev and count for each column in a train_set
def summarize_dataset(train_set):
    summaries=[(mean(column), stdev(column), len(column)) for column in zip(*train_set)]
    del(summaries[-1])
   
    return summaries

#split train_set by class then calculate statistics for each row
def summarize_by_class(train_set):
    separated=separate_by_class(train_set)

 
    summaries=dict()
    for class_value,rows in separated.items():
        summaries[class_value]=summarize_dataset(rows)
        
    return summaries

#calculate the probabilities of prdictiong each class for a given row
def calculate_probability(x,mean, stdev):
    exponent=exp(-((x-mean)**2/(2*stdev**2)))
    return (1/(sqrt(2*pi)*stdev))*exponent

# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])     
   
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
  
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, _ = class_summaries[i]
			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
	return probabilities
 
# Predict the class for a given row
def predict(summaries, row):
	probabilities = calculate_class_probabilities(summaries, row)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label

def navie_bayes(train,test):
    global summaries
    summaries=summarize_by_class(train)
    predictions=list()
    for row in test:
        output=predict(summaries, row)
        predictions.append(output)
    return predictions

def navie_bayesoutput(aa):
    aa=sum(aa,[])
    predicted=(predict(summaries, aa))
    print("navies bayes")
    print(predicted)
    return predicted
