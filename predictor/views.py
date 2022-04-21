from django.shortcuts import render
from  predictor.algorithms import main
from predictor.models import Datas

# Create your views here.
def prediction(request):
    template_name = "prediction/predict.html"
    return render(request, template_name)

def process(request):
    data=[]
    name = request.POST["name"]
    age = request.POST["age"]
    print(age)
    data.append(age)
    gender = request.POST["gender"]
    polyuria = request.POST["polyuria"]
    polydipsia = request.POST["polydipsia"]
    weight_loss = request.POST["weight_loss"]
    weakness = request.POST["weakness"]
    polyphagia = request.POST["polyphagia"]
    genital_thrush = request.POST["genaital_thrush"]
    visual_blurring = request.POST["visual_blurring"]

    irritability = request.POST["irritability"]   
    
    partial_paresis = request.POST["partial_paresis"]
    muscle_stiffness = request.POST["muscle_stiffness"]
    alopecia = request.POST["alopecia"]

    data.extend([gender, polyuria, polydipsia, weight_loss, weakness, polyphagia, genital_thrush, visual_blurring, irritability, partial_paresis, muscle_stiffness, alopecia])
    data = [data]
    prediction, accuracy = main.main(data)
    # print(prediction)
    # print(name)
    d = Datas(name=name, age=age, gender=gender, polyuria=polyuria, polydipsia=polydipsia, weight_loss=weight_loss, weakness=weakness, polyphagia=polyphagia, genital_thrush=genital_thrush, visual_blurring=visual_blurring, irritability=irritability, partial_paresis=partial_paresis, muscle_stiffness=muscle_stiffness, alopecia=alopecia, result_random_forest=prediction[0], result_decision_tree=prediction[1] ,result_naive_bayes=prediction[2] ,result_knn=prediction[3] ,result_logistic_regression=prediction[4] ,result_svm=prediction[5] )
    d.save()
    for result in prediction:
        message = ""
        n_count = 0
        p_count = 0
        if result == "Negative":
            n_count += 1
        else:
            p_count += 1
        if n_count >= p_count:
            result = "Negative"
            message = "No necessary of consultant with doctor"
        else :
            result = "Positive"
            message = "You should contact with the consultant soon"
    print (message)

    return render(request, "prediction/single_result.html",{"prediction":prediction, "accuracy":accuracy, "message":message, "name":name, "age":age, "result":result})

   
        