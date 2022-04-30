## 1. Install and setup
https://www.tableau.com/products/desktop </br>
Apply 1 year student license: https://www.tableau.com/academic/students

## 2. Follow this video Tutorial
https://www.tableau.com/learn/tutorials/on-demand/getting-started?playlist=365020

## 3. Call python script for clustering algorithm processing (Airbnb dataset)
- Install and test Tabpy library 
> pip install tabpy <br>
Type> tabpy <br>
Test running by open browser at "localhost:9004"

### Final result
![image](https://user-images.githubusercontent.com/69342162/165112595-fcd6444e-cdc5-47a7-b87f-51c8108faf20.png)


```python

STR(SCRIPT_REAL("
                
import numpy as np
import numpy.ma as ma
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans,  MiniBatchKMeans, AffinityPropagation
                
print('Start')
                
# Scaling Features
sc= StandardScaler()
avg_price = sc.fit_transform(np.array(_arg1).reshape(-1,1))
print(avg_price)
med_review = sc.fit_transform(np.array(_arg2).reshape(-1,1))
med_beds = sc.fit_transform(np.array(_arg3).reshape(-1,1))
n_cl = _arg4[0]
                
# Combine Scaled feature
X_comb = np.column_stack([avg_price, med_review, med_beds])

# Handling null value with masked array
X = np.where(np.isnan(X_comb), ma.array(X_comb, mask=np.isnan(X_comb)).mean(axis=0), X_comb)
                
# Modeling
result = []
if _arg5[0]==1:
    kmeans = KMeans(n_clusters = n_cl, random_state=99)
    result = kmeans.fit_predict(X).tolist()
elif _arg5[0]==2:
    minib = MiniBatchKMeans(n_clusters = n_cl, random_state=99)
    result =  minib.fit_predict(X).tolist()
else:
    aff = AffinityPropagation().fit(X)
    result = aff.predict(X).tolist()

print(result)

return result
",
AVG([Price]),
MEDIAN([Review Scores Rating]),
MEDIAN([Beds]),
[Cluster Numbers],
[Clustering Algorithm]
))


```
