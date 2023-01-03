# pc-components-stock-monitor

<p style="text-justify">A web application that shows the stock information of PC components (e.g., CPUs, GPUs). The webpage is implemented in <code>Flask</code> and users can filter, sort, and search for a specific type of hardware. A <code>Scrapy</code> application is running at the backend to collect data periodically. Data will be stored in a <code>MongoDB</code> instance, and newly collected data will update the existing records in the MongoDB and the latest update time will be provided. Currently, the application is only collecting <code>graphic card</code> stock, but it will be developed to collect stock information for other hardware such as CPUs and memory.</p>

<p style="text-justify">Each component (i.e., web app, spider, database) of this application is <code>containerized</code>. In terms of development, a single docker-compose file can be used to specify the dependencies between components and to run the application by invoking <code>docker compose up</code>. A CI pipeline has been created to test the application and build the Docker images and push the images to Docker Hub. These images can then be used to deploy the application on some container services or Kubernetes clusters.</p>

## Main Page

<img src="https://github.com/sjyangkevin/pc-components-stock-monitor/blob/main/images/main_page.png">

## How to run the application locally

<p style="text-justify">To run the application on local, first clone the repository</p> 
<p style="text-justify">Then, copy the <code>.env.template</code> file, and rename it as <code>.env</code>. This file will be used to configure the <code>docker-compose.yaml</code> file to run the application. Fill up the following configuration</p>

<ul>
  <li><code>MONGO_INITDB_ROOT_USERNAME</code>: username for login / connect to the MongoDB</li>
  <li><code>MONGO_INITDB_ROOT_PASSWORD</code>: password for login / connect to the MongoDB</li>
  <li><code>MONGO_INITDB_DATABASE</code>: database for storing the collected data</li>
  <li><code>ME_CONFIG_BASICAUTH_USERNAME</code>: username for login to the Mongo Express</li>
  <li><code>ME_CONFIG_BASICAUTH_PASSWORD</code>: password for login to the Mongo Express</li>
  <li><code>PRODUCT_COLLECTION</code>: the collection used to storing the collected data</li>
  <li><code>SECRET_KEY</code>: the secret key for the Flask application</li>
  <li><code>IMAGE_DOWNLOAD_PATH</code>: the path to store the downloaded images regarding the collected items </li>
</ul>

<p style="text-justify">After that, go to the project root directory, and run <code>docker compose up</code></p>
<p style="text-justify">Lastly, after all the services start running, go to the browser and visit <code>http://localhost:5000/</code></p>

## Future Works
<ul>
  <li>Refactoring the project structure and make the configuration more cleaner</li>
  <li>Incorporate more hardware information</li>
  <li>Build better CI/CD pipeline, and complete the application deployment workflow</li>
</ul>
