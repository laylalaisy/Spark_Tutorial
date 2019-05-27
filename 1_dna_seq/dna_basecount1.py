## Spark Application - execute with spark-submit
 
## Imports
from pyspark import SparkConf, SparkContext
 
## Module Constants
APP_NAME = "dna_basecount1"
 
## Closure Functions

## Main functionality
 
def main(sc):
    pass
 
if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
 
    # Execute Main functionality
    recs = sc.textFile('./dna_seq.txt')
    recs.collect()

    ones = recs.flatMap(lambda x: [(c, 1) for c in list(x)])

    baseCount = ones.reduceByKey(lambda x, y: x+y)
    result = baseCount.collect()

    print(result)

