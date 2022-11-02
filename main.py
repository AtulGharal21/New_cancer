from flask import Flask,request,render_template
import json
import pickle
with open("model.pickle","rb") as f:
    model=pickle.load(f)
    
with open("std.pickle","rb") as f:
    std=pickle.load(f)

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=request.form
    
    mean_radius=float(data["mean radius"])
    mean_texture=float(data["mean texture"])
    mean_perimeter=float(data["mean perimeter"])
    mean_area=float(data["mean area"])
    mean_smoothness=float(data["mean smoothness"])
    mean_compactness=float(data["mean compactness"])
    mean_concavity=float(data["mean concavity"])
    mean_concave_points=float(data["mean concave points"])
    mean_symmetry=float(data["mean symmetry"])
    mean_fractal_dimension=float(data["mean fractal dimension"])
    radius_error=float(data["radius error"])
    texture_error=float(data["texture error"])
    perimete_error=float(data["perimeter error"])
    area_error=float(data["area error"])
    smoothness_error=float(data["smoothness error"])
    compactness_error=float(data["compactness error"])
    concavity_error=float(data["concavity error"])
    concave_points_error=float(data["concave points error"])
    symmetry_error=float(data["symmetry error"])
    fractal_dimension_error=float(data["fractal dimension error"])
    worst_radius=float(data["worst radius"])
    worst_texture=float(data["worst texture"])
    worst_perimeter=float(data["worst perimeter"])
    worst_area=float(data["worst area"])
    worst_smoothness=float(data["worst smoothness"])
    worst_compactness=float(data["worst compactness"])
    worst_concavity=float(data["worst concavity"])
    worst_concave_points=float(data["worst concave points"])
    worst_symmetry=float(data["worst symmetry"])
    worst_fractal_dimension=float(data["worst fractal dimension"])

    
    input_data=[[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,
                mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimete_error,area_error,smoothness_error,
                compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,
                worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,
                worst_symmetry,worst_fractal_dimension]]
    
    std_input=std.transform(input_data)
    
    result=model.predict(std_input)
    
    return render_template("index.html",result=result)
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)