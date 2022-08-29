from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import col, substring
import datetime
import re



spark = SparkSession.builder \
    .master("local") \
        .appName("product_data") \
            .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

product_file_df = spark.read.option("header", True).option("inferSchema", True).csv("file:/home/nithia_justin/p2_Team4_Data.csv")



#Mengistu
product_info = product_file_df.select(["product_category", "country", "qty"])
product_info.createOrReplaceTempView("product")

# Changing a string to integer 
# StructField('qty', StringType(), nullable=True),
# item_df.withColumn('qty', item_df['qty'].cast("int"))

# What is the top selling category of items? Per country?
    
print("================================= top selling product category =================================================")

top_selling_product_category = spark.sql("SELECT  DISTINCT product_category, SUM(qty) AS total FROM  product  WHERE qty > 0 AND product_category IS NOT NULL AND product_category IS NOT NULL GROUP BY  product_category ORDER BY total DESC ")
top_selling_product_category.show()

print("===================================== top selling product category per country ==================================")

top_selling_product_category_per_country = spark.sql("SELECT  DISTINCT product_category,  country, SUM(qty) AS total FROM  product  WHERE qty > 0 AND country IS NOT NULL AND product_category IS NOT NULL GROUP BY country, product_category ORDER BY country, total DESC ")
top_selling_product_category_per_country.show()

print("  ++++ SORTED +++++")
sorted = top_selling_product_category_per_country.sort( F.desc("total")).show()


#Benjamin
popularity_simple = product_file_df.select(["product_name","product_category", "qty", "datetime", "country"])

popularity_simple.createOrReplaceTempView("popularity_simple")
category_df = spark.sql("SELECT DISTINCT product_name as pn, product_category as pc FROM popularity_simple WHERE product_category !='null' ORDER BY pn")

category_df.createOrReplaceTempView("category_df")

summary_df = spark.sql("SELECT pc, sum(qty) as Sold, IFNULL(DATE_FORMAT(datetime, 'MMM'), SUBSTRING_INDEX(SUBSTRING_INDEX(datetime,',',2),' ',-1)) AS Month, country FROM popularity_simple JOIN category_df ON pn=product_name WHERE qty != -1000 AND pc IN ('history', 'fiction', 'nonfiction') GROUP BY pc, country, Month ORDER BY pc, country, Month")
summary_df.show(13)



#Nithia
#quantity_filter = "qty in ('(random.random()*20 + 1).__round__()')"
quantity_filter = "qty in ('1','2','3','4','5','6','7','8','9','10')"
txn_id_regex = "(?i)[a-z]{2}\-[0-9]{6}"
valid_countries = ['United States', 'Italy', 'Nigeria', 'England', 'Spain', 'France', 'Germany', 'Portugal', 'Japan', 'Mexico']

clean_df = product_file_df.filter(quantity_filter).filter(col("country").isin(valid_countries))

clean_df.createOrReplaceTempView("clean_df")
final_df_0 = spark.sql("select country,count(product_name) as Sales from clean_df group by country order by sales Desc")
#final_df_0 = spark.sql("select country,sum(qty) as Sales from clean_df group by country order by sales Desc")
final_df_0.show(50)


#Aaniq
item_category = product_file_df.withColumn("year", substring("datetime", 1, 10)).withColumn("hour", substring("datetime", 11, 12))
item_category = item_category.withColumn("hr", substring("hour", 1, 3)).withColumn("second", substring("datetime", 4, 8))

item_category = item_category.drop("year")
item_category = item_category.drop("hour")
item_category = item_category.drop("second")


item_category.createOrReplaceTempView("sales")


traffic_selling = spark.sql("SELECT DISTINCT  hr, SUM(qty) AS total FROM  sales  WHERE qty > 0  AND  left(datetime, 1 ) = 2 GROUP BY  hr ORDER BY  total DESC ")
traffic_selling.show()

print("THE HIGHEST SALES TRAFFIC PER COUNTRY")
date_selling = spark.sql("SELECT DISTINCT country, hr, SUM(qty) AS high FROM  sales  WHERE qty > 0   AND  left(datetime, 1 ) = 2 GROUP BY  country, hr ORDER BY country, high DESC")
date_selling.show()


top_selling_product_category_per_country.repartition(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/p2/p2_Team4_Output_Data_ctry")
top_selling_product_category.repartition(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/p2/p2_Team4_Output_Data_cat")
summary_df.coalesce(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/p2//country_month")
final_df_0.coalesce(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/p2/Country_other_team")
traffic_selling.repartition(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/p2/p2_Team4_Output_Data_p2_traffic")
date_selling.repartition(1).write.csv("file:/mnt/c/Users/Nithia Justin/Desktop/p2/p2_Team4_Output_Data_p2_date")
spark.stop()