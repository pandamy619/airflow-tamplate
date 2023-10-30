"""Test the validity of all DAGs."""

from airflow.models import DagBag


def test_dagbag():
    dag_bag = DagBag(include_examples=False)
    
    assert not dag_bag.import_errors

    for dag_id, dag in dag_bag.dags.items():
        error_message = f"{dag_id} in {dag.full_filepath} has no tags"
        assert dag.tags, error_message
