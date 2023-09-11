import streamlit as st
from graphviz import Digraph

# Create a Digraph object
dot = Digraph(comment="Four Boxes with Arrows")

# Add nodes (boxes)
dot.node('A', 'Box A')
dot.node('B', 'Box B')
dot.node('C', 'Box C')
dot.node('D', 'Box D')

# Add edges (arrows)
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'A')

# Show the diagram in Streamlit
st.graphviz_chart(dot.source)

