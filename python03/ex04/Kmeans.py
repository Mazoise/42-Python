import sys
from numpy import genfromtxt
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def show_clusters(self, X):
        """
        Show the clusters.
        """
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('Height')
        ax.set_ylabel('Weight')
        ax.set_zlabel('Bone_density')
        colors = ['r', 'g', 'b', 'y']
        for i in range(self.ncentroid):
            ax.scatter(X[self.clusters[i]][:, 0],
                       X[self.clusters[i]][:, 1],
                       X[self.clusters[i]][:, 2],
                       c=colors[i])
            ax.scatter(self.centroids[i][0],
                       self.centroids[i][1],
                       self.centroids[i][2],
                       c=colors[i], marker='*')
        plt.show()

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids,
        random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        if type(X) is not np.ndarray:
            return None
        centroid_idx = np.array((random.sample(range(len(X)),
                                k=self.ncentroid)))
        self.centroids = np.array([X[idx] for idx in centroid_idx])
        for i in range(self.max_iter):
            if i is not 0 and (old_centroids == self.centroids).all():
                break
            old_centroids = np.copy(self.centroids)
            self.predict(X)
            for k in range(self.ncentroid):
                self.centroids[k] = np.mean(X[self.clusters[k]], axis=0)
        if (self.ncentroid == 4):
            self.show_clusters(X)
        print("Centroid populations:")
        for k in range(self.ncentroid):
            print(k, ":", len(self.clusters[k]))

    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        # ... your code ...
        self.clusters = list([] for i in range(self.ncentroid))
        ret = np.zeros(len(X), dtype=int)
        for j in range(len(X)):
            min_dist = sys.maxsize
            min_idx = None
            for k in range(self.ncentroid):
                dist = sum(abs(X[j][idx] - self.centroids[k][idx])
                           for idx in range(len(X[j])))
                if dist < min_dist:
                    min_dist = dist
                    min_idx = k
            self.clusters[min_idx].append(j)
            ret[j] = min_idx
        return ret


def main(**kwargs):
    try:
        assert len(kwargs) is 3, "Wrong number of arguments"
        filepath = kwargs['filepath']
        ncentroid = int(kwargs['ncentroid'])
        max_iter = int(kwargs['max_iter'])
        kmean = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
        csv_file = genfromtxt(filepath, delimiter=',',
                              skip_header=1, usecols=(1, 2, 3))
        kmean.fit(csv_file)
        print("Population repartition:")
        print(kmean.predict(csv_file))
    except KeyError:
        print("Error : Wrong argument keys, expecting\
 filepath, ncentroid, max_iter")
    except AssertionError as e:
        print("Error :", e)
    except ValueError:
        print("Error : Wrong argument values")
    except OSError as e:
        print("Error :", e)


if __name__ == '__main__':
    main(**dict(arg.split('=') if '=' in arg
         else ['', ''] for arg in sys.argv[1:]))
