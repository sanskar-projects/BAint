import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("customer_reviews.csv")
r=df.shape[0]
r1=df.query("Recommended=='yes'").shape[0]
x=np.array(["positive\nfeedback"])
y=np.array([r1])
plt.bar(x,y,color="green")
r2=df.query("Recommended=='no'").shape[0]
x=np.array(["negative\nfeedback"])
y=np.array([r2])
plt.bar(x,y,color="red")
plt.title("Analysis of customer reviews")
plt.show()

s="&Recommended=='yes'"
r1=df.query("Traveller_type=='Family Leisure'"+s).shape[0]
r2=df.query("Traveller_type=='Solo Leisure'"+s).shape[0]
r3=df.query("Traveller_type=='Couple Leisure'"+s).shape[0]
r4=df.query("Seat_type=='Economy Class'"+s).shape[0]
r5=df.query("Seat_type=='Business Class'"+s).shape[0]
r6=df.query("Seat_type=='First Class'"+s).shape[0]
x=np.array(["Family\nLeisure\n(+)","Solo\nLeisure\n(+)","Couple\nLeisure\n(+)"])
y=np.array([r1,r2,r3])
plt.bar(x,y,color="green")

s="&Recommended=='no'"
r1=df.query("Traveller_type=='Family Leisure'"+s).shape[0]
r2=df.query("Traveller_type=='Solo Leisure'"+s).shape[0]
r3=df.query("Traveller_type=='Couple Leisure'"+s).shape[0]
x=np.array(["Family\nLeisure\n(-)","Solo\nLeisure\n(-)","Couple\nLeisure\n(-)"])
y=np.array([r1,r2,r3])
plt.bar(x,y,color="red")
plt.title("Analysis of customer reviews by Traveller_type")
plt.show()

s="&Recommended=='yes'"
r4=df.query("Seat_type=='Economy Class'"+s).shape[0]
r5=df.query("Seat_type=='Business Class'"+s).shape[0]
r6=df.query("Seat_type=='First Class'"+s).shape[0]
x=np.array(["Economy\nClass\n(+)","Business\nClass\n(+)","First\nClass\n(+)"])
y=np.array([r4,r5,r6])
plt.bar(x,y,color="green")

s="&Recommended=='no'"
r4=df.query("Seat_type=='Economy Class'"+s).shape[0]
r5=df.query("Seat_type=='Business Class'"+s).shape[0]
r6=df.query("Seat_type=='First Class'"+s).shape[0]
x=np.array(["Economy\nClass\n(-)","Business\nClass\n(-)","First\nClass\n(-)"])
y=np.array([r4,r5,r6])
plt.bar(x,y,color="red")
plt.title("Analysis of customer reviews by Seat_type")
plt.show()
