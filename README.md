<img width="933" alt="title" src="https://user-images.githubusercontent.com/105242871/184061095-31e3bfc0-a2f1-44de-8b5e-417d51d5e444.png">

# 🟦 Class Demos & Resources

## 1️⃣ Acquisition and Preparation
- Acquire a sample of data from SQL.
- Identify null values, which nulls are 'deal-breakers', i.e. rows removed, which nulls should be represented by 0, and which should be replaced by a     value from other methods, such as mean.
- Identify outliers and decide what to do with them, if anything (remove, keep as-is, replace).
- Data Structure: Aggregate as needed so that every row is an observation and each column is a variable (1 variable and not a measure).

  [Wrangle](wrangle_lesson.ipynb)

  [Outliers: To Drop or Not to Drop](https://www.theanalysisfactor.com/outliers-to-drop-or-not-to-drop/)

  [Tidy Data](https://github.com/nickhould/tidy-data-python)
## 2️⃣ Exploration
- Can we see patterns, find signals in the data?

- What features are driving the outcome?

- Are there other features we can construct that have stronger relationships?

- Use Visualization and statistical testing to help answer these questions.

- We want to walk away from exploration with with modeling strategies (feature selection, algorithm selection, evaluation methods, for example).
  
  [Explore](explore_lesson.ipynb)

## 3️⃣ Modeling
◾ **K-Means**

  **Algorithm**:
  - Start with our data: X.
  - Randomly1 choose k points in the same space as X. These are called the centroids.
  - Calculate the distance from every point in X to each of the centroids.
  - Assign each point in X to the closest centroid.
  - Reposition the centroids such that they are the average of all the points assigned to them.
  - Repeat from step 3 until some condition for stopping2 is met.

  **Vocabulary**:
  - *centroid*: one of the cluster centers in a K-Means clustering
  - *inertia*: sum of the squared distances from each point to it's assigned centroid

  **Further Reading:**
  
  [Elbow Method](https://en.wikipedia.org/wiki/Elbow_method_(clustering))
  
  [Determining the number of clusters in a data set](https://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set)
  
  [scikit-learn User Guide: KMeans](https://scikit-learn.org/stable/modules/clustering.html#k-means)
  
◾ **Density Based Clustering: DBSCAN**

- Stands for “Density Based Spatial Clustering of Applications with Noise”.
- Does not require the user to set the number of clusters a priori.
- Can capture clusters of complex shapes.
- Can identify points that are not part of any cluster (very useful as outliers detector).
- Is somewhat slower than agglomerative clustering and K-means, but still scales to relatively large datasets.
- Works by identifying points that are in crowded regions of the feature space, where many data points are close together (dense regions in feature       space).
- Points that are within a dense region are called core samples (or core points).
- There are two parameters in DBSCAN: min_samples and eps.
- If there are at least min_samples many data points within a distance of eps to a given data point, that data point is classified as a core sample.
- Core samples that are closer to each other than the distance eps are put into the same cluster by DBSCAN.

  [Modeling](modeling_lession.ipynb)

## 4️⃣ Using Clusters
- Explore Your Clusters
- Turn Your Clusters into Labels
- Model Each Cluster Separately
- Turn your Clusters into Features

  [Using Clusters](using_clusters_lesson.ipynb)

***
# 🟦 Exercises
## 1️⃣ Acquisition and Preparation
[Zillow](zillow.ipynb)

[Zillow Functions: wrangle_zillow](wrangle_zillow.py)

[Mall Customers](mall_customers.ipynb)

[Mall Functions: wrangle_mall](wrangle_mall.py)

## 2️⃣ Exploration
[Explore](explore_zillow.ipynb)

## 3️⃣ Modeling
[Modeling](modeling.ipynb)

***
# 🟦 Project

[How Accurate Is Your Zestimates?](https://github.com/m3redithw/zestimates-clustering-project)
