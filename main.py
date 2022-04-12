import streamlit as st
import matplotlib.pyplot as plt

""" 1, 入参 """
number = st.number_input('number', None)
text = st.text_input('text', None)
""" 2， 中间过程 """
def turn(x,y):
    result = str(int(x)) + ' ' + y
	return result
result = turn(number, text)
result = {'result':result}

  
""" 3, 出参 """
st.write(result)


""" 4, 补充一个绘图，说不定以后能用到 """
st.markdown("# matplotlib绘图")  # 带#是一级标题，字体会大一点，一般仅设置到3级标题
x_plot = [i for i in range(int(number))]
y_plot = [2*j for j in range(int(number))]

plt.figure()
plt.plot(x_plot, y_plot)
st.pyplot()    # 其实就是 plt.show()  这里不能直接写plt.show()
