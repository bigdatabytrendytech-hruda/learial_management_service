from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CustomerNthSalary") \
    .getOrCreate()

# Load the customer.csv file
file_path = "customer.csv"  # Update with the correct path to your CSV file
customer_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Define the nth salary to retrieve
n = 2  # Replace with the desired nth value

# Create a window specification to partition by customer and order by salary descending
window_spec = Window.partitionBy("customer_id").orderBy(col("salary").desc())

# Add a row number column to rank salaries for each customer
ranked_df = customer_df.withColumn("rank", row_number().over(window_spec))

# Filter to get only the nth salary for each customer
nth_salary_df = ranked_df.filter(col("rank") == n).drop("rank")

# Show the result
nth_salary_df.show()

# Stop the Spark session
spark.stop()