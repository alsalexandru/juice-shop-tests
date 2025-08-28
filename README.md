# Juice Shop Tests

Test framework (UI/AI/Security) for OWASPs Juice-Shop

## Setting Up the Application

To run the application locally, you can use Docker. Follow the steps below:

1. Ensure you have Docker installed on your machine.
2. Use the following command to start the Juice Shop application in a Docker container:

   ```bash
   sudo docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop
   ```

   - `sudo`: Ensures the command runs with elevated privileges (only needed if your Docker setup requires it).
   - `docker run`: Command to start a Docker container.
   - `-d`: Runs the container in detached mode (in the background).
   - `--name juice-shop`: Assigns the container a name (`juice-shop`).
   - `-p 3000:3000`: Maps port `3000` on your local machine to port `3000` in the container.
   - `bkimminich/juice-shop`: The image name to pull and run.

3. Once the container is running, the application will be available at:  
   **[http://localhost:3000/](http://localhost:3000/)**

### Verifying the Setup

- Open your browser and visit **http://localhost:3000/**.  
- You should see the Juice Shop homepage loaded, confirming that the application is running.

---
## Install prerequisites for test framework

To set up and run the project, follow these steps:

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:

   ```bash
   python -m playwright install
   ```
---

## Running Tests

  ```bash
  pytest -n auto \
  --html=reports/report.html \
  --self-contained-html \
  --junit-xml=reports/test_results.xml \
  --browser firefox \
  --headed \
  --base-url=http://localhost:3000
  ```
### Explanation of Command Options:

- **`-n auto`**  
  *Enables parallel test execution using `pytest-xdist`.*  
  - `auto` automatically detects the number of available CPU cores and runs the tests in parallel using all available cores.  
  - This significantly speeds up the test execution time, especially for large test suites.
  - **Alternate Option**: Instead of `auto`, you can specify an integer (e.g., `-n 4`) to set the number of parallel workers manually.  
    - This is useful if you want to limit the number of cores being used, based on your setup.  
    - The maximum value for this number depends on the number of CPU cores available on your machine.  


- **`--self-contained-html`**  
  *Create a self-contained html file containing all necessary styles, scripts, and images*


- **`--html=path/to/report.html`**  
  *Generates an HTML test report.*  
  - This option saves a detailed test execution report in HTML format, which is helpful for reviewing results visually.


- **`--junit-xml=path/to/junit.xml`**  
  *Generates a JUnit-style XML test report.*  
  - This option saves the test execution results in JUnit XML format, which can be used for CI/CD pipelines (e.g., Jenkins or other tools that consume JUnit reports).  


- **`--browser`**
  - **Example Values**: `firefox`, `chromium`, or `webkit`.  
  - In this command, the browser used is **Firefox**.  
  - **Default**: If not provided, Playwright uses `chromium`.  


- **`--headed`**  
  *Runs the browser in headed mode.*  
  - By default, Playwright runs tests in **headless mode** (no browser window is visible).  
  - Adding this option opens the browser window so you can visually observe the test execution.  


- **`--base-url`**  
  *Specifies the base URL for the tests.*  
  - **Example Value**: `http://localhost:3000`.  
  - The base URL is used by the test suite for relative navigation, allowing flexibility to test across different environments (e.g., local, staging, or production) without modifying the test code.
