import streamlit as st
from graphviz import Digraph

col1, col2,col3,col4,col5,col6 = st.columns(6)
col1.write("This is column 1 and here is some details about it HERE IS THE DATE 35/5325/5 and some presecription: do this and that ")
col2.write("This is column 2 and here is some details about it HERE IS THE DATE 35/5325/5 and some presecription: do this and that")
col3.write("This is column 3 and here is some details about it HERE IS THE DATE 35/5325/5 and some presecription: do this and that")
col4.write("This is column 4 and here is some details about it HERE IS THE DATE 35/5325/5 and some presecription: do this and that")
col5.write("This is column 5 and here is some details about it HERE IS THE DATE 35/5325/5 and some presecription: do this and that")
col6.write("This is column 6 and here is some details about it HERE IS THE DATE 35/5325/5 and some presecription: do this and that")
               
# # Create a Digraph object
# dot = Digraph(comment="Four Boxes with Arrows")

# # Add nodes (boxes)
# dot.node('A', 'Box A')
# dot.node('B', 'Box B')
# dot.node('C', 'Box C')
# dot.node('D', 'Box D')

# # Add edges (arrows)
# dot.edge('A', 'B')
# dot.edge('B', 'C')
# dot.edge('C', 'D')
# dot.edge('D', 'A')

# # Show the diagram in Streamlit
# st.graphviz_chart(dot.source)

