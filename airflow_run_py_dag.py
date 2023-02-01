from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def run_script1():
    exec(open("/path/to/script1.py").read())

def run_script2():
    exec(open("/path/to/script2.py").read())

def run_script3():
    exec(open("/path/to/script3.py").read())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 2, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sample_dag',
    default_args=default_args,
    description='DAG to execute three Python scripts in sequence',
    schedule_interval=timedelta(hours=1),
)

script1_task = PythonOperator(
    task_id='run_script1',
    python_callable=run_script1,
    dag=dag,
)

script2_task = PythonOperator(
    task_id='run_script2',
    python_callable=run_script2,
    dag=dag,
    depends_on_past=True,
)

script3_task = PythonOperator(
    task_id='run_script3',
    python_callable=run_script3,
    dag=dag,
    depends_on_past=True,
)

script1_task >> script2_task >> script3_task
