# Get shape of Series using shape attribute
import pandas as pd
pd.Series( ["Spark","PySpark","Hadoop","Python","pandas","Oracle"] )
courses = pd.Series( ["Spark","PySpark","Hadoop","Python","pandas","Oracle"] )
print(courses.shape)