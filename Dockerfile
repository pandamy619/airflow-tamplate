FROM apache/airflow:2.7.2

RUN pip install --upgrade pip
RUN pip install poetry==1.5.1

COPY poetry.lock pyproject.toml ./

RUN poetry install --without dev --no-root
