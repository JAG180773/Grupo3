# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 03:21:17 2024

@author: jagon
"""
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import streamlit as st

st.title('Grupo # 3 - Trabajo Final Grupal 2024 - 2')
st.write('Hola **como** estas')
appointment = st.slider(label = 'Programe Horario de asesoria',
                        value= (time(11,30), time(12,45)))
