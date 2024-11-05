import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from ml_model import predict_writing_level
from rubrics import rubrics_benchmark


result = predict_writing_level(writing_composition='hello world')

print(result)



rubrics_assessment = rubrics_benchmark("hello world")

print(rubrics_assessment.Benchmark_result())

