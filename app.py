import streamlit as st
import joblib

# Load model
with open('final_model.joblib', 'rb') as file:
    model = joblib.load(file)

def prediction(inp_list):
    pred = model.predict([inp_list])[0]
    if pred == 0:
        return 'Sitting on bed'
    elif pred == 1:
        return 'Sitting on chair'
    elif pred == 2:
        return 'Lying on bed'
    else:
        return 'Ambulating'

def main():
    st.title('ACTIVITY PREDICTION FROM SENSOR DATA')
    st.subheader('''
        This application will predict the ongoing activity based on the sensor data provided. 
        Fill in the respective fields and it will be predicted.
    ''')
    st.image('image.webp')
    
    rfid = st.selectbox('Enter the RFID configuration settings',
                        ['Config 1 (4 Sensors)', 'Config 2 (3 Sensors)'])
    rfid_e = 3 if rfid == 'Config 2 (3 Sensors)' else 4

    ant_ID = st.selectbox('Select the Antena ID', [1,2,3,4])
    rssi = st.text_input('Enter the received signal strength indicator (RSSI)')
    accv = st.text_input('Enter the vertical acceleration data from sensor')
    accf = st.text_input('Enter the frontal acceleration data from sensor')
    accl = st.text_input('Enter the lateral acceleration data from sensor')

    if st.button('Predict'):
        try:
            # Convert to the correct types
            inp_data = [
                float(accf),
                float(accv),
                float(accl),
                int(ant_ID),
                float(rssi),
                int(rfid_e)
            ]
            response = prediction(inp_data)
            st.success(response)
        except ValueError:
            st.error("Please ensure all numerical fields are filled with valid numbers.")

if __name__ == '__main__':
    main()
