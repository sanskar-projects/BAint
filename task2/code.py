import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

data_set=pd.read_csv("customer_booking_processed.csv")

x=data_set.iloc[:,[0,1,2,3,4,5,6,9,10,11,12]].values
y=data_set.iloc[:,13].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

st_x=StandardScaler()
x_train=st_x.fit_transform(x_train)
x_test=st_x.transform(x_test)

classifier=RandomForestClassifier(n_estimators=10,criterion="entropy")
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)


cm=confusion_matrix(y_test,y_pred)
tn,fp,fn,tp=cm.ravel()
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

print("Customer buying behaviour prediction{random forest model}")
print("\nTrue values\n=true negatives+true positives\n={}+{}\n={}\n\nFalse values\n=false positives+false negatives\n={}+{}\n={}".format(tn,tp,tn+tp,fp,fn,fp+fn))
mtp.title("Confusion matrix")
mtp.show()
