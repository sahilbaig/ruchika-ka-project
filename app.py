import re
from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv (r"C:\Users\sahil\Downloads\sample.csv")
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/search" , methods=["GET","POST"])
def search():
    if request.method=="POST":
        df = pd.read_csv (r"C:\Users\sahil\Downloads\sample.csv" , low_memory=False)
        data_recieved=request.form.get("search_val")
        df = pd.DataFrame(df, columns= [
    'gr_id',
    'sap_id',
    'sfdc_id',
    'sales_organization',
    'name',
    'house_number',
    'postcode',
    'street',
    'city',
    'sfdc_tenure',
    'sfdc_tier',
    'simulation_subtype',
    'cluster',
    'quadrant',
    'sfdc_rtm',
    'segment',
    'sub_segment',
    'poc_image',
    'oneyp_volume',
    'volume_potential_3',
    'strategic_relevance',
    'salesforce_status',
    'volume_survey_total_abi',
    'account_type',
    'salesforce_channel',
    'sub_channel',
    'visit_frequency'])
    
        df_new = df[df['sap_id'] == data_recieved]
        return render_template("search.html", tables=[df_new.to_html(classes='data', header="true")])    

    return render_template("search.html")

@app.route("/complete")
def complete():
    columnNames=(list(df.columns))
    completenessList=[]
    for i in columnNames:
        completenessList.append({"val1":df[i].notnull().sum(),"val2":len(df[i]),"name":i})
        # (df[i].notnull().sum(),"/",gr_id_val)

    return render_template('complete.html',completenessList=completenessList)