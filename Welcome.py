import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import toml

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='PHI02_Q3', page_icon='\U0001F412')


st.header(":gear: Welcome to :violet[PHI02: **Introduction to Classical Mechanics II**] :gear:")
st.caption('-by Physics Meerkat :ringed_planet:')

st.markdown(
    '''
### Scope ของคอร์ส: :violet[**Introduction to Classical Mechanics II**]    
* :violet[**Linear Momentum Principle:**]   
ใน Zone นี้เราศึกษา Translations ของ อนุภาค/ระบบอนุภาค ผ่าน :blue[Linear Momentum] โดยมีหัวข้อสำคัญดังนี้.      
    - :red[Momentum - Impulse Theorem.]
    - :red[Principle of Conservation of Linear Momentum.]
    - :red[Center of Masses and Collisions.]
* :violet[**Dynamics of Rotation and Angular Momentum:**]   
ใน Zone นี้เราศึกษา Rotation ตั้งแต่เริ่มต้นจนพัฒนาไปถึงแนวคิดของ :blue[Angular Momentum]. หัวข้อสำคัญมีดังนี้:   
    - :red[Kinematics of Rotations.]   
    - :red[Newton's $2^{nd}$ Law for Rotation.]   
    - :red[Torque and Angular Momentum.]   
    - :red[Principle of Conservation of Angular Momentum.]
* :violet[**Fluid Mechanics:**]   
ใน Zone นี้เราเริ่มนำ :blue[Principles of Mechanics] ไป apply กับระบบต่างๆ โดยระบบแรกที่เราสนใจคือ :blue[Fluid]. หัวข้อสำคัญมีดังนี้:   
    - :red[Pressure and Buoyancy.]   
    - :red[Pascal's Principle.]   
    - :red[The Continuity Equation.]   
    - :red[Bernoulli's Principle.]
'''
)

st.divider()

st.subheader('Lectures')

Lecture = [
    'Linear Momentum and Impulse. ❌', 'Conservation of Linear Momentum and Collisions. ❌', 'Problem Solving for Linear Momentum I. ✅', 'Problem Solving for Linear Momentum II. ❌',
    'Kinematics of Rotation. ✅', 'Energy in Rotating Systems and Moment of Inertia. ✅','Torque and Angular Accelerations. ❌','The Angular Momentum. ❌','Additional Problems for Angular Momentum. ❌',
    'Fluid Mechanics I - Statics (Pressure and Buoyancy). ❌', 'Fluid Mechancics II - Dynamics (The Continuity and Bernoillis Equations). ❌','Additional Problems for Fluid Mechanics. ❌',
    'Principles of Mechanics - Final Lecture. ❌'
]

pages_name = ['welcome', '1 linear momentum and impulse', '2 conservation of linear momentum', '3 problems for linear momentum i', '4 problems for linear momentum ii', '5 kinematics of rotations', '6 energy in rotating systems', '7 turque and angular accelerations', '8 the angular momentum', '9 problems for angular momentum', '10 fluid mechanics i - statics', '11 fluid mechanics ii - dynamics', '12 problems for fluid mechanics', '13 principles of mechanics']

switch_button = []
for i in range(len(Lecture)):
    switch_button.append(st.button(label='**{}: {}**'.format(i+1,Lecture[i]),use_container_width=True))
    
    if switch_button[i]:
        st.write('You just click thebutton:', Lecture[i])
        switch_page(pages_name[i+1])


st.divider()

