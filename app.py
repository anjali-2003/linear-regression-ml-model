import pickle
import streamlit as st
  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(km_driven, mileage,  max_power, age, Diesel, Electric, LPG, Petrol, Manual, seats5, more5seats):  
   
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
    <h1 style ="color:black;text-align:center;">ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    km_driven = st.text_input("km_driven")
    mileage = st.text_input("mileage")
    max_power = st.text_input("max_power(in horse power)")
    age = st.text_input("age(in years)")
    st.subheader("choose your vehicle properties")
    a = st.checkbox('Diesel')
    if a:
        Diesel = 1.0
    else:
        Diesel = 0.0
    a = st.checkbox('Electric')
    if a:
        Electric = 1.0
    else:
        Electric = 0.0
    a = st.checkbox('LPG')
    if a:
        LPG = 1.0
    else:
        LPG = 0.0
    a = st.checkbox('Petrol')
    if a:
        Petrol = 1.0
    else:
        Petrol = 0.0
    a = st.checkbox('Manual')
    if a:
        Manual = 1.0
    else:
        Manual = 0.0
    a = st.checkbox('seats5')
    if a:
        seats5 = 1.0
    else:
        seats5 = 0.0
    a = st.checkbox(' more than 5seats')
    if a:
        more5seats = 1.0
    else:
        more5seats = 0.0
        
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction( float(km_driven), float(mileage), float(max_power), float(age), float(Diesel), float(Electric), float(LPG), float(Petrol), float(Manual), float(seats5), float(more5seats))
    st.success('The output(in lakhs) is {}'.format(result))
     
if __name__=='__main__':
    main()