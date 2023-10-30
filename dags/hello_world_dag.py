from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from tasks.hello_world.hello_world import print_hello


default_args = {
    'description': 'Hello World DAG',
    'schedule_interval': '*/5 * * * *',
    'start_date': datetime(2022, 4, 20), 
    'catchup': False,
}

with DAG('hello_world_every_5_minutes', default_args=default_args) as dag:
    start_task = DummyOperator(task_id='start_task')
    
    hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
    
    end_task = DummyOperator(task_id='end_task')

start_task >> hello_operator >> end_task