# Deploy

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.local.env.yml** -- environment for your application. For example, you have some databases and some servicese, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.local.full.yml** -- full application with environment
* **docker-compose.prod.yml** -- this is docker-compose for deploy to production
* **docker-compose.stage.yml** -- this is docker-compose for deploy to stage. Stage and production have difference between ports
* **docker-compose.test-runner.yml** -- this is file which run tests for your application and shoots to the application (docker-compose.local.full.yml)

For each docker-compose we have environment file into `./.env` directory.
