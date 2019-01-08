# SPOTLIGHT: Detecting Anomalies in Streaming Graphs
---

This is the implementation of "SPOTLIGHT: Detecting Anomalies in Streaming Graphs." published by Dhivya Eswaran et al. in KDD 2018.  
You can access full paper from the link below.  
<https://www.kdd.org/kdd2018/accepted-papers/view/spotlight-detecting-anomalies-in-streaming-graphs>

* spotlight_darpa.ipynb  
an example of the application of spotlight to Darpa 1998 test dataset(tcpdump files).
In the paper, they used RRCF(Robust Random Cut Trees) for the calculation of anomaly scores, but I used Isolation Forests instead.

* spotlight.py  
input file should be csv file consists of Nx3 array.  
first column: source IP node  
second column: destination node  
third column: timestamp  
this python file loads input communication log file, sketches it to spotlight space, and save vectors data. 
