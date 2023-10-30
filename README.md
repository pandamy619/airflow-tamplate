<p align="center">
  <a href="https://airflow.apache.org/" rel="noopener">
 <img width=200px height=200px src="./icons/Airflow_logo.png" alt="Airflow logo"></a>
</p>

<h3 align="center">TASK SERVER</h3>

---

<p align="center"> Task server description.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Installing](#installing)
- [Running](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.

## 🏁 Getting Started <a name = "getting_started"></a>
  ### Before you begin
  1. Install Docker Compose v1.29.1 and newer on your workstation.
  2. Created in `dags`, `tasks`, `logs`, `plugins` and `.env`
      ```bash
        mkdir -p ./dags ./dags/tasks ./logs ./plugins
        echo -e "AIRFLOW_UID=$(id -u)" > .env
      ```

## Installing <a name = "installing"></a>

#### Initialize the database
On all operating systems, you need to run database migrations and create the fir st user account. To do it, run.
```bash
docker-compose up airflow-init
```

## 🚀 Running Airflow <a name = "deployment"></a>

```bash
docker-compose up
```

## 🎈 Usage <a name="usage"></a>

[Webserver](http://localhost:8080) The default account has the login `airflow` and the password `airflow`

## 💭 Developer convention
- [DAGs](./docs/DAGS.md) The dags writing convention
- [Branch](./docs/Branch.md) The branch name convention
- [Commit](./docs/Commit.md) The commit message convention
- [Dependencies](./docs/InstallDependencies.md) Installing dependencies

## ⛏️ Built Using <a name = "built_using"></a>

- [PostgreSQL](https://www.postgresql.org/) - Database
- [Airflow](https://airflow.apache.org/) - Task server
- [Redis](https://redis.io/) - Message broker
- [Poetry](https://python-poetry.org/) - Package manager

