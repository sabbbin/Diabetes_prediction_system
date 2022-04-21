#import library
from math import exp
from random import seed
from random import randrange
from csv import reader
from pathlib import Path
# import import_ipynb
import copy
#end of importing library
#inmport algorithm function 
from predictor.algorithms.logisticregression import (logistic_regression, logistic_regressionoutput)
from predictor.algorithms.knnalgorithm import (k_nearest_neighbors,k_nearest_neighborsoutput)
from predictor.algorithms.naviebayes import (navie_bayes,navie_bayesoutput)
from predictor.algorithms.decisiontree import (decision_tree,decision_treeoutput)
from predictor.algorithms.randomforest import (random_forest, random_forestoutput)
from predictor.algorithms.svm import (svmalgorithm,svmalgorithmoutput)
#end of importing algorithm function

#creating dict form algorithm
algorithm={ 0:random_forest,1:decision_tree, 2:navie_bayes,3:k_nearest_neighbors, 4:logistic_regression,5:svmalgorithm}
outcomepredicted={ 0:random_forestoutput,1:decision_treeoutput, 2:navie_bayesoutput,3:k_nearest_neighborsoutput, 4:logistic_regressionoutput,5:svmalgorithmoutput}
#creating dict form attributes of dataset
convert={'Male':1,'Female':0,'Yes':1,'No':0, 'Positive':1, 'Negative':0}
#creating dict for output
outputpredict={0:'Negative',1:'Positive'}

#load a CSV file
def load_database(filename):
	dataset = list() #creating a list of dataset
	with open(filename, 'r') as file: #opening file in readmode
		csv_reader = reader(file) #reading file in iterable form
	
		for row in csv_reader:
			
			if not row:
				continue
			dataset.append(row) #appending the row in form of a\rray
	return dataset # returning of the file
#end of reading of dataset

#mapping to male and femal
def mapping(dataset):
    for i in range(len(dataset[0])): #finding the lenght of column of dataset
        for row in dataset: # getting each row  in succcessive order
            for i in range(len(row)): # making iteration in row
           
                if convert.get(row[i])!=None: #checking the convert dictionary
                    row[i]=convert[row[i]] # mapping with convert dictionary if staisfied
                else :
                    row[i]=float(row[i]) #convert  the string into float if not satisfied
#end of mapping

#feature selection:                  
def cutting (dataset):

    for row in dataset: #iterating database by each row
        
        row.remove(row[9]) #removing  Itching attribute of dataset
    
       
        row.remove(row[10])#removing delayed healing attribute of dataset
        row.remove(row[13])# removing obesity attribute of dataset
    
    
        
    

#convert string column to float
def convert_str_to_float(dataset):
 
    for i in range(len(dataset[0])):#ffinding the lenth of column of dataset
        for row in dataset:# iterating the dataset by each row
            row[i]=float (row[i].strip()) #converting the string into float
# end of converion of string to float

#calculatin mean of each column and update zero value column
def calcuate_mean(dataset):
    for i in range (len(dataset[0])-1): #finding the length of column of dataset except the last one
        sum=0.0 # calcualting the total sum of column
        count=0 # calculating the total count of value
        missingindex=[] # storing the missing index  of column
        for row in dataset: # reading teh database by row
            if row[i] != None: #checking if row is  not None
                sum+=row[i] # calculating the sum of each value
            else:
                missingindex.append(count)   # storing the index of mission column
            count+=1 #increasing count
        avg=sum/count # finding the average
         # updating the mission value in dataset
        for j in range(len(missingindex)):
            dataset[missingindex[j]][i]=avg
# end 
           
           
#find the min and max values of each column
def min_max_dataset(dataset):
    minmax=list() # initializinf the list for minmax
    for i in range(len(dataset[0])-1):
        col_values=[row[i] for row in dataset] # finding the all value of column`
        min_value=min(col_values) # finding the min value of column
        max_value=max(col_values) # finding the max value of column
        minmax.append([min_value, max_value]) # appending the min and max value
    return minmax
#end

# rescale dataset columns to the range to the rane 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset: # reading the dataset_list by row 
        for i in range(len(row)-1):
            row[i]=(row[i]-minmax[i][0])/(minmax[i][1]-minmax[i][0]) # convering the each value between 0-1
#end

#split a dataset into k folds
def cross_validation_split(dataset, n_folds):
    dataset_split=list() # creating the list for dataset_list
    dataset_copy=list(dataset)  #copying the list of dataset so that we can pop data in dublicate dataset
    fold_size=int(len(dataset)/n_folds) # finding the length of dataset for training
    fold=list() # creating list for training
    

    while len(fold)<fold_size: 
        index=randrange(len(dataset_copy)) # finding the random index
        fold.append(dataset_copy.pop(index)) # finding the dataset_row  for training
      
    return dataset_copy, fold
#end

#calculation of accuracy,precison,recall,f1score
def accuracy_metric(actual, predicted):
    truepostive=0 #count for true positive
    truenegative=0 # count for true negative
    falsepostive=0 # count for false positive
    falsenegative=0 # count for false negative
 
    for j in range(len(actual)): # finding the length of actual 
        if actual[j]==1.0: # checking it whether it is positive 
         
           
            if actual[j]==predicted[j]: # checking whether both are true
                truepostive=truepostive+1
            else:
                falsepostive=falsepostive+1 # increasing the count of false positve
        else:
            if actual[j]==predicted[j]: # checking both are false
                truenegative=truenegative+1
            else:
                falsenegative=falsenegative+1 # increasing count of false negative
    accuracy=(truenegative+truepostive)/(len(actual)) # calculating the accuracy
    precision=(truepostive)/(truepostive+falsepostive)
    recall=(truepostive)/(truepostive+falsenegative)
    f1score=2*((precision*recall)/(precision+recall))

    return accuracy,precision,recall,f1score
#end

# initializing array for storing the ouput of predict value of user given data of each algoirthm
# output=[]
#calling different algorithm
def evaluate_algorithm(dataset,n_folds, aa):
    
    train_set ,test_set =cross_validation_split(dataset,n_folds)

    #creating the list for accuray ,precision, recall, f1scores for all algorithms
    accuries=list()
    precisions=list()
    recalls=list()
    f1scores=list()
    output = list()
    #intitializing count for 5 algorithm in dict algorithm
    count=0
  
   
    while(count<6):
        
        
        predicted=algorithm[count](train_set, test_set) # calling each algorithm  and get predicted output of test data
        aaa=outcomepredicted[count](aa)
        aaa=int(aaa)
         #checking the output for  giver user data aa
        output.append(outputpredict[aaa]) # storing the predicted ouptut in outputlist
        actual=[row[-1] for row in test_set] # storing the actual ouptut of test data
      
       
        if count != 0: #if count is not zerot then making the predicted array into anotherarray
            predicted=([predicted])
        # if count == 0:
        #     predicted= sum(predicted,[])
        #     print('abc')
        #     print(predicted)
        # initializing the value of accuracy ,precision,recall,f1score for each algorithm
        accuracy1=0
        precision1=0
        recall1=0
        f1score1=0
        
        count1=0
        for i in range(len(predicted)):
            accuracy,precision,recall,f1score= accuracy_metric(actual, predicted[i]) # calling accuracy metric for test data
            #calculating accuracy, precison ,recall, f1score for random forest
            if count==0:
                accuracy1+=accuracy
                precision1+=precision
                recall1+=recall
                f1score1+=f1score
               
                count1=count1+1
            #calculating accuracy,precision,recall, f1score other algorithm
            else:
                count1=1
                accuracy1=accuracy
                precision1=precision
                recall1=recall
                f1score1= f1score
        #finding average  of accuracy,precison........
        accuracy1=accuracy1/count1
        precision1= precision1/count1
        recall1=recall1/count1
        f1score1=f1score1/count1        
        # accuracy=accuracyy/count1
        # accuracy1.append(accuracy)
        # precision1.append(precision)
        # recall1.append(recall)
        # f1score1.append(f1score)
        # apending accuracy,preions ...... into array
        accuries.append(accuracy1)
        precisions.append(precision1)
        recalls.append(recall1)
        f1scores.append(f1score1)
          
           
        
        count+=1
      
        
    return accuries,precisions,recalls,f1scores, output

#end


def main(data):
    seed(1)
    #load and prepare data
    filename="predictor/algorithms/diabetes.csv"
    dataset=load_database(filename)
    #remove the header column

    cutting(dataset)

    dataset.remove(dataset[0])
    # mapping dataset with numeric value
    mapping(dataset)

    # calculate the mean
    calcuate_mean(dataset)
    #finding the min-max value
    minmax=min_max_dataset(dataset)
    print(minmax)
    #normalization the value
    normalize_dataset(dataset, minmax)

    #calculation the percentage of dataset for training data
    n_folds = 4.5


    # input here
    # bb=([['6','148','72','35','0','33.6','0.627','50']])
    # aa=([['38','Male','No','No','No','No','No','No','No','No','No','No','No']])

    mapping(data)

    normalize_dataset(data,minmax)
    print('abced')
    print(data)


    accuries,precisions,recalls,f1scores,output= evaluate_algorithm(dataset,n_folds,data)


    algorithmpredict={'random_forest':0,'decision-tree':1,'navie-bayes':2,'knn-algorithm':3,'logistic-regression':4}
    # print('Scores: %s' % scores)
    # print('random-forest','decision-tree','navie_bayes','KNN algorithm','logistic-regression')
    # print("output")
    # print('output: %s' % output)
    # print('accuries %s'% accuries)
    # print('precisions %s'%precisions)
    # print('recalls%s' %recalls)
    # print('f1scores%s'%f1scores)
    # #checking the value for random forest
    # print('---------------------------------------------------------------------')
    # print('randomforest%s'%output[algorithmpredict['random_forest']])
    # print('randomforest%s'%accuries[algorithmpredict['random_forest']])
    # print('hhhhh%s'%precisions[algorithmpredict['random_forest']])
    # print('hhhhh%s'%recalls[algorithmpredict['random_forest']])
    # print('hhhhh%s'%f1scores[algorithmpredict['random_forest']])
    filenam= Path.cwd().joinpath('predictor/algorithms/results')
    print(filenam)
    f = open(filenam/'accuracy.txt','w+')
    for a in accuries:
        f.write('%.3f\n' %a)
    f.close()
    f = open(filenam/'precision.txt','w+')
    for a in precisions:
        f.write('%.3f\n' %a)
    f.close()
    f = open(filenam/'recall.txt','w+')
    for a in recalls:
        f.write('%.3f\n' %a)
    f.close()
    f = open(filenam/'f1score.txt','w+')
    for a in f1scores:
        f.write('%.3f\n' %a)
    f.close()
    # f = open(filenam/'result.txt','w+')
    # for a in output:

    #     f.write('%d\n' %convert[a])

    # f.close()

    return output, accuries

# aa=([['38','Male','No','No','No','No','No','No','No','No','No','No']])
# main(aa):