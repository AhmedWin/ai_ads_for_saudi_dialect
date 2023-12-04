import streamlit as st
import pandas as pd
import numpy as np
import random
from io import StringIO
import tweepy
import Post_Tweet
import time

raw_audio = {}
def main(): 
    try:

        st.title('Saudi Dialect')
        st.header('_Clasify_ by Text!', divider='rainbow')
        classes = ['نجدي','حجازي','مصري','تونسي']
        pre_defined_text = "...ارحب تراحيب المطر, تفضل قهوتنا السعودية"
        title = st.text_input('text to classify',pre_defined_text)

        if st.button('Classify text'):
            time.sleep(3)
            if not title:
                st.warning('Please enter text', icon="⚠️")
            else:
                if title == pre_defined_text:
                    st.write('اللهجة المدخلة هي:', "نجدي")
                else:
                    st.write('اللهجة المدخلة هي:', random.choice(classes))

        option = st.selectbox(
        'How would you like to convert the Dialect to?',
        ('Hijazi' , 'Najdi', 'Tunisian','Egyptian'))
        title = st.text_input('Text','ارحب تراحيب المطر, تفضل قهوتنا السعودية')
        dialect_dic = {
            'Hijazi':'📍اعلان\n\nارحب تراحيب المطر، قهوتنا السعودية بين يديك',
            'Najdi':'📍اعلان\n\nارحب تراحيب المطر، قهوتنا السعودية بين يديك',
            'Tunisian': '📍اعلان\n\nارحب تراحيب المطر، قهوتنا السعودية بين يديك',
            'Egyptian': '📍اعلان\n\nارحب تراحيب المطر، قهوتنا السعودية بين يديك'
        }
        if st.button('Convert text'):
            time.sleep(3)
            dialect_dic[option]
            # publish the campaign
        if st.button('publish the campaign'):
            Post_Tweet.post_tweet({"text": "📍اعلان\n\n"+title}) 
    except Exception as ee:
        print("Error", ee)


if __name__=="__main__": 
    main() 