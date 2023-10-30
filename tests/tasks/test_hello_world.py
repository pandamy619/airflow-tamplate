from ...dags.tasks.hello_world.hello_world import print_hello


def test_print_hello_world():
    message = print_hello()
    assert message == 'Hello world from first Airflow DAG!'
