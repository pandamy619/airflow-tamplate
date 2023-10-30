# DAGs

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Testing](#testing)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies.

A DAG is defined in a Python script, which represents the DAGs structure (tasks and their dependencies) as code.

## Getting Started <a name = "getting_started"></a>

Working directory
```bash
├── airflow-task-server
│    ├── dags
|    |   ├── tasks   
│    │   |   └── hello_world
│    │   |          ├── hello_world.py
│    │   └── hello_world_dag.py
|    ├── tests
|    |   ├── dags
|    |   └── tasks

```

Creating a DAG

./tasks/hello_world/hello_world.py
```python
def print_hello():
    return 'Hello world from first Airflow DAG!'
```

./hello_world_dag.py
```python
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from tasks.hello_world.hello_world import print_hello


default_args = {
    'description': 'Hello World DAG',
    'schedule_interval': '0 12 * * *',
    'start_date': datetime(2022, 4, 20), 
    'catchup': False,
}

with DAG('hello_world', default_args=default_args) as dag:
    start_task = DummyOperator(task_id='start_task')
    
    hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
    
    end_task = DummyOperator(task_id='end_task')

start_task >> hello_operator >> end_task
```

## Testing <a name = "testing"></a>

### initialize the database tables
```bash
>>> ./airflow.sh airflow db init
[2022-04-21 09:42:49,601] {db.py:919} INFO - Creating tables
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
WARNI [airflow.models.crypto] empty cryptography key - values will not be stored encrypted.
Initialization done
```
### print the list of active DAGs
```bash
>>> ./airflow.sh airflow dags list
Creating task_server_airflow-cli_run ... done
dag_id        | filepath            | owner   | paused
==============+=====================+=========+=======
<your_dag_id> | <your_file_name>.py | airflow | True
```
### prints the list of tasks in the "task" DAG
```bash
>>> ./airflow.sh airflow tasks list <task_id>
Creating task_server_airflow-cli_run ... done
# Shows tasks in your dag 
end_task 
start_task 
```

### prints the hierarchy of tasks in the "task" DAG
```bash
>>> ./airflow.sh airflow tasks list <task_id> --tree
Creating task_server_airflow-cli_run ... done
# Shows tasks in your dag 
<Task(DummyOperator): start_task>
    <Task(DummyOperator): end_task>
```

### unit testing of tasks
```python
from ...dags.tasks.hello_world.hello_world import print_hello


def test_print_hello_world():
    message = print_hello()
    assert message == 'Hello world from first Airflow DAG!'
```

## Contributing <a name = "сontributing"></a>

