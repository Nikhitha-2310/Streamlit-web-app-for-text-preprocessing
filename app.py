import streamlit as st
import pandas as pd
import re
import emoji

with st.sidebar:
    radio_button=st.radio('characters',['lower case','html tags','urls','hashtags','mentions','unwanted characters','emojis','All'])
    
    
st.title('Text Preprocessing')

file=st.file_uploader('Upload csv file', type='csv')
st.write('Upload a CSV file containing 1 feature with text data')
check_button=st.button('Check')
remove_button=st.button('Remove')



if(file and check_button):
    df=pd.read_csv(file,names=['Reviews'])
    def eda3(data,column):
        lower=' '.join(data[column]).islower()
        html=data[column].apply(lambda x: True if re.search('<.*?>',x) else False).sum()
        urls=data[column].apply(lambda x: True if re.search('http[s]?://.+?\S+',x) else False).sum()
        hasht=data[column].apply(lambda x: True if re.search('#\S+',x) else False).sum()
        mentions=data[column].apply(lambda x: True if re.search('@\S+',x) else False).sum()
        un_c=data[column].apply(lambda x: True if re.search("[]\.\*'\-#@$%^(0-9)]",x) else False).sum()
        emojiss=data[column].apply(lambda x: True if emoji.emoji_count(x) else False).sum()
        if(lower==False):
            st.write('Your data contains lower and upper case')
        if(html>0):
            st.write("Your data contains html tags")
        if(urls>0):
            st.write("Your data contains urls")
        if(hasht>0):
            st.write("Your data contains hashtags")
        if(mentions>0):
            st.write("Your data contains mentions")
        if(un_c):
            st.write("Your data contains unwanted chars")
        if(emojiss):
            st.write("Your data contains emojis")

    eda3(df,'Reviews')

if(file and remove_button and radio_button=='All'):
    df=pd.read_csv(file,names=['Reviews'])
    def basic_pp(x,emoj="F"):
        if(emoj=="T"):
            x=emoji.demojize(x)
        x=x.lower()
        x=re.sub('<.*?>',' ',x)
        x=re.sub('http[s]?://.+?\S+',' ',x)
        x=re.sub('#\S+',' ',x)
        x=re.sub('@\S+',' ',x)
    
        x=re.sub("[]\.\*'\-,_?#@$%^(0-9):]",' ',x)
        return x
        
    processed_review=df['Reviews'].apply(basic_pp,args=("T"))
    for i in processed_review:
        st.write(i)


if(file and remove_button and radio_button=='lower case'):
    df=pd.read_csv(file,names=['Reviews'])
    def lower_case(x):
        x=x.lower()
        return x
    
    for i in df['Reviews'].apply(lower_case):
        st.write(i)


if(file and remove_button and radio_button=='urls'):
    df=pd.read_csv(file,names=['Reviews'])
    def urls(x):
        x=re.sub('http[s]?://.+?\S+',' ',x)
        return x
    
    for i in df['Reviews'].apply(urls):
        st.write(i)

if(file and remove_button and radio_button=='html tags'):
    df=pd.read_csv(file,names=['Reviews'])
    def html_tags(x):
        x=re.sub('<.*?>',' ',x)
        return x
    
    for i in df['Reviews'].apply(html_tags):
        st.write(i)

if(file and remove_button and radio_button=='hashtags'):
    df=pd.read_csv(file,names=['Reviews'])
    def hash_tags(x):
        x=re.sub('#\S+',' ',x)
        return x
    
    for i in df['Reviews'].apply(hash_tags):
        st.write(i)

if(file and remove_button and radio_button=='mentions'):
    df=pd.read_csv(file,names=['Reviews'])
    def mentions(x):
        x=re.sub('@\S+',' ',x)
        return x
    
    for i in df['Reviews'].apply(mentions):
        st.write(i)


if(file and remove_button and radio_button=='unwanted characters'):
    df=pd.read_csv(file,names=['Reviews'])
    def unwanted_chars(x):
        x=re.sub("[]\.\*'\-,_?#@$%^(0-9):]",' ',x)
        return x
    
    for i in df['Reviews'].apply(unwanted_chars):
        st.write(i)


if(file and remove_button and radio_button=='emojis'):
    df=pd.read_csv(file,names=['Reviews'])
    def emojiss(x,emoj='F'):
        if(emoj=="T"):
            x=emoji.demojize(x)
        return x
    
    for i in df['Reviews'].apply(emojiss,args="T"):
        st.write(i)


    
    


