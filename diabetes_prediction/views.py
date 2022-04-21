from django.shortcuts import render, HttpResponse
from json import dumps 
import csv
from predictor.models import Datas

def home(request):
    template_name = "index.html"
    return render(request, template_name)



def send_dictionary(request): 
    # create data dictionary 
  

    
    filename='predictor/algorithms/results/'
   
    with open (filename+'accuracy.txt', 'r',encoding='utf-8') as file:
        accuracy= list(map(float, file.readlines()))
    file.close() 
   
    with open (filename+'f1score.txt', 'r',encoding='utf-8') as file:
        f1score= list(map(float, file.readlines()))
    file.close()
    with open (filename+'precision.txt', 'r',encoding='utf-8') as file:
        precision= list(map(float, file.readlines()))
    file.close()
    with open (filename+'recall.txt', 'r',encoding='utf-8') as file:
        recall= list(map(float, file.readlines()))
    file.close()
    with open (filename+'result.txt', 'r', encoding='utf-8') as file:
	
        result=list(map(int,file.readlines()))
    file.close()

    dataDictionary= {
        'accuracy':accuracy,
        'f1score':f1score,
        'precision': precision,
        'recall':recall,
        'result':result

    }
    print(accuracy)
        
    dataJSON = dumps(dataDictionary) 
    return render(request, 'partials/comparison.html', {'data': dataJSON})


def dataset(request):
    return render(request, "partials/dataset.html")

def export_csv(request):
    response = HttpResponse(content_type='text/csv')  

    writer = csv.writer(response)   
    writer.writerow(['Age','Gender','Polyuria','Polydipsia','Sudden weight loss','Weakness','Polyphagia','Genital thrush','visual blurring','Irritability','partial paresis','muscle stiffness','Alopecia','Random Forest','Decision Tree','Naive Bayes','KNN','Logistic Regression','SVM'])

    for data in Datas.objects.all().values_list('age','gender','polyuria','polydipsia','weight_loss','weakness','polyphagia','genital_thrush','visual_blurring','irritability','partial_paresis','muscle_stiffness','alopecia','result_random_forest','result_decision_tree','result_naive_bayes','result_knn','result_logistic_regression','result_svm'):
        writer.writerow(data)

    response['Content-Disposition'] = 'attachment; filename="users_data.csv"'
    return response


