from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

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
    description='DAG to execute three shell scripts in sequence',
    schedule_interval=timedelta(hours=1),
)

script1_task = BashOperator(
    task_id='run_script1',
    bash_command='/path/to/script1.sh',
    dag=dag,
)

script2_task = BashOperator(
    task_id='run_script2',
    bash_command='/path/to/script2.sh',
    dag=dag,
    depends_on_past=True,
)

script3_task = BashOperator(
    task_id='run_script3',
    bash_command='/path/to/script3.sh',
    dag=dag,
    depends_on_past=True,
)

script1_task >> script2_task >> script3_task




