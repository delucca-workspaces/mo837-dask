# MO837 Dask

This repository is an exploration over Dask for UNICAMP's MO837 class. It is organized into different branches, where each branch represents a part of the exploration itself.

## Getting started

This application executes a Dask workflow using a distributed cluster. In this section you'll learn how to setup the dependencies, install the application requirements, launch the cluster, and execute the application

### Installing dependencies

To execute the application you need to install the following dependencies:

- [poetry](https://python-poetry.org/docs/#installation)

### Installing application requirements

After installing all dependencies, you can run the following command (at the root folder of this repository):

```bash
poetry install
```


This will install all Python requirements for this application

### Launching the cluster

To launch the cluster, you must first builder the Docker image with the following command:

```bash
poetry run hpccm --recipe cluster/recipe.py --format docker > cluster/Dockerfile
```

Now that you have the Dockerfile built, you can execute the following command to launch your cluster:

```bash
docker-compose up -d --scale worker=<num_workers>
```

> *Warning*
>
> You can set the num_workers variable to whatever number pleases you. This will be used by docker-compose to scale the number of workers

### Launching the application

Now that everything is properly working, you can run the application with the following command:

```bash
poetry run python src/app.py --scheduler_url localhost:9000
```

> *Warning*
>
> If you don't want to execute it on the cluster, you can simply don't pass anything for the `--scheduler_url` argument

Congrats! You were able to execute a Dask workflow using a distributed approach 🥳
