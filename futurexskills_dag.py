from datetime import datetime, timedelta
from textwrap import dedent
print("futurexskills example DAG")

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

default_args={
    "owner": "futurexskills",
    "retries": 1,
	"retry_delay":timedelta(minutes=2)
}

with DAG(
    "futurexskills_dag",
    default_args = default_args,
    description = "first dag",
    start_date=datetime(2023, 1, 11, 2),
    schedule='@daily'
) as dag:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="echo futurexskills success"
    )
    t1
    
