#calculate the euclidean distance between two vectors
from math import sqrt
def euclidean_distance(row1, row2):
    distance=0.0
    for i in range (len(row1)-1):
        distance+=(row1[i]-row2[i])**2
    return sqrt(distance)

def get_neighbors(train,test_row, num_neighbors):
    distance=list()
    for train_row in train:
        dist=euclidean_distance(test_row, train_row)
        distance.append((train_row,dist))
    distance.sort(key=lambda tup:tup[1])
    neighbors=list()
    for i in range(num_neighbors):
        neighbors.append(distance[i][0])
    return neighbors

def predict_classification(neighbors):
    output_values=[row[-1] for row in neighbors]
    prediction=max(set(output_values), key=output_values.count)
    return prediction
num_neighbors=11
def k_nearest_neighbors(train,test):
    global train1
    train1=train
    
    prediction=list()
    for row in test:
        neighbors=get_neighbors(train, row,num_neighbors)
        output=predict_classification(neighbors)
        prediction.append(output)
       
    return (prediction)

def k_nearest_neighborsoutput(aa):
    aa=sum(aa,[])
    predicted=get_neighbors(train1,aa,num_neighbors)
    output1=predict_classification(predicted)
    print('nkk anlgoirt')
    print(output1)
    return output1