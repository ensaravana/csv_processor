import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.page_link("./pages/calculation.py", label="Page  Refresh") 
st.write(st.session_state)
if "authentication_status" not in st.session_state:
    st.switch_page("./app.py")

st.sidebar.button("Logout",key="nga",on_click = st.session_state.logout)

 
    
def callme():
    file = st.file_uploader("upload your file",type=['csv','xlsx'])
    if file is not None:
        if file.name.split(".")[1] == "csv":
            file2 = pd.read_csv(file)
        if file.name.split(".")[1] == "xlsx":
            file2 = pd.read_excel(file)
        # elif file.name.split(".")[1] == "xlsx" or file.name.split(".")[1] == "csv":
        #     st.warning("only csv and excel  allowed")    
        excel_data1 = pd.DataFrame(file2,dtype="object")
        s= {
             
         }
        a = pd.DataFrame(s)
        options = st.multiselect("Selection the column",excel_data1.columns)
        metrices = ["dates", "month", "years", "quarter"]
        selection = st.segmented_control(
             "Select Metrices", metrices, selection_mode="multi"
         ) 
        # print(selection)
        if st.button("Submit"):
            print(excel_data1["Created Time"],"naga")
            res1 = excel_data1["Created Time"].astype(str)  
            print(res1)
            split_values = res1.str.split(" ")  
            result_data = split_values.tolist()
            dates = []
            month= []
            years = []
            time = []
            quarter = []
            for i in result_data:
                for j in i:
                    if "/" in j:
                        a1,a2,a3 = j.split("/")
                        date = f"{a2}-{a1}-{a3}"
                        mon = f"{a1}-{a3}"
                        yea = a3
                        dates.append(date)
                        month.append(mon)
                        years.append(yea)
                        if int(a1) >= 4 and int(a1) <= 6:
                            quarter.append(f'Q1-{a3}')
                        if int(a1) >= 7 and int(a1) <= 9: 
                            quarter.append(f'Q2-{a3}')
                        if int(a1) >= 10 and int(a1) <= 12:
                            quarter.append(f'Q3-{a3}')
                        if int(a1) >= 1 and int(a1) <= 3:
                            quarter.append(f'Q4-{a3}')     

                    if ":" in j:
                        time.append(j)
            # print(dates,month,years,quarter)     
            for select in selection:
                z=0
                if select == "dates":            
                    a.insert(loc=z,column="Dates",value=np.array(dates) )
                    z=+1  
                    # print(z,"1")
                if select == "month":    
                    a.insert(loc=z,column="Month",value=np.array(month) )
                    z=+1
                    # print(z,"2")
                if select == "years": 
                    a.insert(loc=z,column="Year",value=np.array(years) )
                    z=+1
                    # print(z,"3")
                if select == "quarter":    
                    a.insert(loc=z,column="Quarter",value=np.array(quarter) )
                    z=+1
                    # print(z,"4")
            count = z
            # print(count,"count")  

            for name in excel_data1.columns:  
                 numb = count
                 for op in options:
                      if name == op: 
                        #    st.table(excel_data1[name])
                           a.insert(loc=numb,column=op, value=np.array(excel_data1[name]))
                           numb=+1
                        #    print("nth number")
            # print(a)  
            @st.cache_data
            def convert_df(df):
                return df.to_csv(index=False).encode('utf-8')
            csv = convert_df(a)

            st.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
            )
                        
                           
        # if any(options):
        #    
      
        # a.insert(loc=0, column='django-score',
        #  value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
        # a.insert(loc=1, column='score',
        #  value=np.array([0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
        
        # print(a)
      
        
      
            # # try:
           

        # except :
        #    raise TypeError ( st.write("Some error is found in your file"))


        

        
     
      
            


                


      
        # r2 = res1.split(" ")
        # print
        # d1 = pd.Series(data = r2 , index = file2.columns ,name = 1)
        # print(d1)

callme()    

        # excel_data1['data'] = d1
        # arr = []
        # for i in file2.columns: 
        #     arr.append(i)
        # k1 = st.multiselect("select",arr)

        # data = file2.columns  
        # for i in data:
        #     st.checkbox(i)

# fig = px.bar(x=["a","b","c"],y=[1,2,3])
# st.plotly_chart(fig)  



                          

