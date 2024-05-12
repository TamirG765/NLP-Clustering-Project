# Text Clustering Application for Patent Analysis

## Introduction
This application is designed to analyze and group patent claims into topics, enhancing understanding of the mobile communications sector. It leverages advanced text processing techniques to dynamically cluster patent texts based on user input regarding the desired number of groups. The backend is built with FastAPI and integrates with a Streamlit frontend for a user-friendly interactive experience.

## Getting Started

### Prerequisites
To run this application, you'll need Python installed on your machine.

### Setup Environment

1. **Clone the Repository**:
    Clone the repository to your local machine using the following command:
    ```bash
    git clone <https://github.com/TamirG765/home-assignment-ml>

2. **Navigate to the Project Directory**:
    ```bash
    cd HomeAssignmentML

3. **Create a Virtual Environment**:
    * For conda:
    ```bash
    conda create -n myenv 
    conda activate myenv
    ```

    * Other option:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Dependencies**:
    With your Conda environment activated, install the required Python packages specified in `requirements.txt`:
    ```bash
    pip install -r requirements.txt

## Running the Application
__Note: the env should stay activated!__

1. **Navigate to the FastAPI App Directory**:
   Open a terminal window and navigate to the directory where FastAPI app is located:
   ```bash
   cd HomeAssignmentML/App
   ```

2. **Run the FastAPI Server**:
    Start the server using uvicorn with the following command:
    ```bash
    uvicorn fast_app:app --reload
    ```

This starts the backend server on `http://localhost:8000`.
Note: Ensure this matches the URL configured in your Streamlit app.

3. **Run the Streamlit App**
    Open another terminal window and navigate to the directory where the Streamlit app is located:
    ```bash
    cd HomeAssignmentML/App
    ```
This will open the Streamlit interface in your default web browser, typically accessible at `http://localhost:8501`.
