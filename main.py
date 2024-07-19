from sklearn import tree

clf = tree.DecisionTreeClassifier()

# Ma'lumotlarni Yig'amiz
# Quyoshli Kunlar, Yomg'irli Kunlar, Sovuq Kunlar

x = [
    [134, 34, 190], [78, 124, 190],
    [67, 56, 246], [245, 10, 90],
    [46, 134, 246], [236, 45, 50],
    [344, 5, 10], [167, 47, 124],
    [135, 46, 157], [178, 178, 20]
]
y = ['Yaxshi', 'Yomon', "O'rtacha", 'Yaxshi', 'Yomon', 'Yaxshi', 'Yaxshi', "O'rtacha", 'Yahshi', 'Yahshi']

clf = clf.fit(x, y)

Natija = clf.predict([[235, 67, 78]])
print(Natija)
