from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F


def create_spark_session(name: str) -> SparkSession:
    """Creates a SparkSession with a pre-defined configuration.

    Args:
        name (str): The name of the application for the SparkSession.

    Returns:
        SparkSession: A SparkSession object configured with default settings.

    This function creates a SparkSession with the following configuration options:

    * spark.driver.bindAddress: 127.0.0.1 (Binds the driver to localhost)
    * spark.driver.host: 127.0.0.1 (Sets the driver's hostname)
    * spark.executor.memory: 4g (Allocates 4 gigabytes of memory to executors)
    * spark.executor.cores: 4 (Sets the number of cores for each executor)
    * spark.sql.default.partition: 10 (Sets the default number of partitions for DataFrame operations)
    * spark.metrics.conf.*.sink.prometheusServlet.class: org.apache.spark.metrics.sink.PrometheusServlet (Enables Prometheus metrics reporting)
    * spark.metrics.conf.*.sink.prometheusServlet.path: /metrics (Sets the path for the Prometheus metrics endpoint)
    * spark.metrics.conf.*.source.jvm.class: org.apache.spark.metrics.source.JvmSource (Enables collection of JVM metrics)

    These settings provide a reasonable starting point for many Spark applications. You can customize them further by passing additional configuration options to the `SparkSession.builder.config()` method within the function.

    **Note:** While the SparkSession is automatically stopped when the JVM exits, you can explicitly stop it using `spark.stop()` if needed.
    """
    spark_config = {
      "spark.executor.memory": "4g",
      "spark.executor.cores": "4",
      "spark.sql.default.partition": "10",
      "spark.metrics.conf.*.sink.prometheusServlet.class": "org.apache.spark.metrics.sink.PrometheusServlet",
      "spark.metrics.conf.*.sink.prometheusServlet.path": "/metrics",
      "spark.metrics.conf.*.source.jvm.class": "org.apache.spark.metrics.source.JvmSource",
      "spark.ui.prometheus.enabled": "true"
    }

    spark = SparkSession \
      .builder \
      .appName("Write raw data to parquet") \
      .master("spark://0.0.0.0:7077") \
      .config(spark_config) \
      .getOrCreate()

    return spark

def write_raw_data_to_parquet(data_source_uri: str, data_output_uri: str) -> None:
    """
    Writes raw data from a CSV file to a Parquet file.

    Args:
        data_source_uri (str): The URI of the CSV file to read from. The file must have a header row.
        data_output_uri (str): The URI of the Parquet file to write to.
    """
    try:
        spark = SparkSession \
          .builder \
          .appName("Write raw data to parquet") \
          .getOrCreate()

        dataframe = spark.read.csv(data_source_uri, header=True)

        window_spec = Window.partitionBy("Status").orderBy(F.desc("Qty"))
        ranked_data = dataframe.withColumn("rank", F.rank().over(window_spec))

        ranked_data.printSchema()

        dataframe.write.parquet(data_output_uri)

        while True:
            pass

        # spark.stop()
    except Exception as e:
        print(f"Error executing write to parquet: {e}")
        raise e
