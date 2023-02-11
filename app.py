import pickle
import streamlit as st
  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(km_driven, mileage, max_power, age, Diesel, Electric, LPG, Petrol, Manual, seats5, more5seats):  
   
    prediction = classifier.predict(
        [[km_driven, mileage, max_power, age, Diesel, Electric, LPG, Petrol, Manual, seats5, more5seats]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Car Price Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Classifier ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    km_driven = st.slider("km_driven",0,1000000000,0)
    mileage = st.slider("mileage", 0,40,0)
    max_power = st.slider("max_power", 0,200,0)
    age = st.slider("age", 0,20,0)
    Diesel = st.radio("Diesel", ('Yes', 'No'))
    Electric = st.radio("Electric", ('Yes', 'No'))
    LPG = st.radio("LPG", ('Yes', 'No'))
    Petrol = st.radio("Petrol", ('Yes', 'No'))
    Manual = st.radio("Manual", ('Yes', 'No'))
    seats5 = st.radio("seats5", ('Yes', 'No'))
    more5seats = st.radio(">5seats", ('Yes', 'No'))
    result =""
      
    if Diesel == "Yes":
        Diesel=1
    else:
        Diesel=0
    if Electric == "Yes":
        Electric=1
    else:
        Electric=0
    if LPG == "Yes":
        LPG=1
    else:
        LPG=0
    if Petrol == "Yes":
        Petrol=1
    else:
        Petrol=0
    if Manual == "Yes":
        Manual=1
    else:
        Manual=0
    if seats5 == "Yes":
        seats5=1
    else:
        seats5=0
    if more5seats == "Yes":
        more5seats=1
    else:
        more5seats=0
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(float(km_driven), float(mileage), float(max_power), float(age), float(Diesel), float(Electric), float(LPG), float(Petrol), float(Manual), float(seats5), float(more5seats))
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()