# Spark with Prometheus Monitoring in Docker

This project demonstrates how to run a Spark application in a Dockerized environment with Prometheus monitoring. 

**Key Features:**

- **Dockerized Spark:** Includes Docker Compose for easy deployment and management of Spark Master and Worker containers.
- **Prometheus Monitoring:** Configures Spark to expose Prometheus metrics.
- **Metrics Endpoint:** Exposes Prometheus metrics on localhost on ports 8080 and 8081 at the path `/metrics`.

**Prerequisites:**

- Docker and Docker Compose installed and running.
- Java and Scala (if required for your Spark applications) installed on your host machine.

**Getting Started:**

1. **Clone this repository:**
   ```bash
   git clone <repository_url>
   ```

2. Build and run Docker containers:

  ```bash
   cd <repository_directory>
   docker-compose up -d
  ```

3. Verify Spark Master and Worker status:

 - Check the Docker logs for any errors.
 - Access the Spark Master UI in your browser (typically at http://localhost:8080).

4. Access Prometheus Metrics:

 - Use a Prometheus client (e.g., curl, Prometheus server) to scrape metrics from:
    - http://localhost:8080/metrics
    - http://localhost:8081/metrics

## Project Structure:

 - docker-compose.yml: Defines the Docker Compose configuration for Spark Master and Worker containers.
 - spark/conf/: Contains Spark configuration files (e.g., spark-defaults.conf).
 - spark/application.py: (Example) A sample PySpark application.

## Prometheus Configuration (in spark/conf/spark-defaults.conf):

```
spark.metrics.conf.*.sink.prometheusServlet.class org.apache.spark.metrics.sink.PrometheusServlet
spark.metrics.conf.*.sink.prometheusServlet.path /metrics
spark.metrics.conf.*.source.jvm.class org.apache.spark.metrics.source.JvmSource
```

## Note:

 - This is a basic example. You may need to adjust the configuration and application code based on your specific requirements.
 - For production environments, consider using a more robust image for Spark and implement security measures.
 - Explore advanced monitoring and alerting options with Prometheus and tools like Grafana.

## Contributing:

Contributions are welcome! Please feel free to submit pull requests or open issues.

This README provides a basic overview of the project. Please refer to the code and comments within the files for more detailed information.