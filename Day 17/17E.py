from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
label_name = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']
print("label names:", label_name)
print(labels[0])
print(feature_names[0])
print(features[0])
# organizing data into sets
from sklearn.model_selection import train_test_split

train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.40, random_state=42)
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
model = gnb.fit(train, train_labels)
preds = gnb.predict(test)
