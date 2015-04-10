#from pyspark.mllib.clustering import GaussianMixture
#from numpy import array
import numpy as np
import scipy.sparse as sps
from pyspark import SparkContext
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.clustering import KMeans
import logging
import re
from numpy import array
from math import sqrt
import datetime

sc = SparkContext("local", "Simple App")
# Load and parse the data
#data = sc.textFile("data/mllib/gmm_data.txt")
#parsedData = data.map(lambda line: array([float(x) for x in line.strip().split(' ')]))

Vocab_size =102661 #72000  #41807 #???
def change_to_sparse(line):
    keys = []
    values = []
    #logger = logging.getLogger("py4j")
    #logger.setLevel(logging.INFO)
    #logger.addHandler(logging.StreamHandler())
    #logger.info("<><<><><><><><><>")

    temp = line.split("{")[1]
    temp = re.sub('}','',temp)
    for item in temp.split(',')[1:]:
        index = int(item.split(':')[0])
        value = float(item.split(':')[1])
        keys.append(index)
        values.append(value)
    #print keys
    #print values
    #logger.info(max(keys))
    return Vectors.sparse(Vocab_size, sorted(keys),values)

start_time = datetime.datetime.now()
logger = logging.getLogger("py4j")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
#logger.info("this works fine>>>>>>>>>>>>>>>>>>>>>")

data = sc.textFile("bigdata_seq")# sparse_reuters")

logger.info(data.count())
 
parsedData = data.map(lambda line: change_to_sparse(line))
#parsedData.saveAsTextFile("totally_test")

logger.info(parsedData.first())

logger.info("this works fine>>>>>>>>>>>>>>>>>>>>>")
# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 4, maxIterations=10,
        runs=10, initializationMode="random")
end_time = datetime.datetime.now()
#logger.info(clusters.predict(parsedData.first()))
#clusters.clusterCenters.saveAsTextFile("spark_cluster_output")
#def error(point):
#    center = clusters.centers[clusters.predict(point)]
#    return sqrt(sum([x**2 for x in (point - center)]))

#WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
#print("Within Set Sum of Squared Error = " + str(WSSSE))

#gmm = GaussianMixture.train(parsedData, 2)
logger.info("total time:"+str(start_time - end_time))
# output parameters of model
#for i in range(2):
#    print ("weight = ", gmm.weights[i], "mu = ", gmm.gaussians[i].mu,
#        "sigma = ", gmm.gaussians[i].sigma.toArray())
