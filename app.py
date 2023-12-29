
import streamlit as stl
import numpy as np
import pickle

pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)
def pridicting_system(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Age):
    parameters = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Age]])
    prediction_result = model.predict(parameters).reshape(1,-1)
    return prediction_result[0].round()

def main():
    stl.header('   ENTER THE FOLLOWING INFORMATION')


    col1,col2 = stl.columns(2)
    with col1:
        Pregnancies = stl.number_input('Pregnancies')
        Glucose = stl.number_input('Glucose')
        BloodPressure = stl.number_input('BloodPressure')
        SkinThickness = stl.number_input('SkinThickness')
    with col2:
        Insulin = stl.number_input('Insulin')
        bmi = stl.number_input('BMI')
        DiabetesPedigreeFunction = stl.number_input('DiabetesPedigreeFunction')
        Age = stl.number_input('Age')
    
    if stl.button('Test'):
        result = pridicting_system(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Age)
        result = result.astype(int)
        if(result == 1):
          stl.write(f'Result: Postive')
        elif(result == 0):
            stl.write(f'Result: Negative')
        else:
            stl.write(f'Result: No Result Found')



if __name__ == '__main__':
    main()