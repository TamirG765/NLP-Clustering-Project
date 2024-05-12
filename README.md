# Grouping Patent Claims Texts - Home Assignment 🏠

## Introduction 👋🏼
This application is designed to analyze and group patent claims into topics, for better understanding of the mobile communications sector.</br>
It uses advanced text processing techniques to dynamically cluster patent claims based on user input regarding the desired number of groups.</br>
The backend is built with FastAPI and integrates with a Streamlit frontend for a user-friendly experience.

## Getting Started 🐍

### Prerequisites
To run this application, you'll need Python (3.12.3) and Conda installed on your machine.

### Setup Environment

1. **Clone the Repository**:
    Clone the repository to your local machine using the following command:
    ```bash
    git clone <https://github.com/TamirG765/home-assignment-ml>
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd HomeAssignmentML
    ```

3. **Create a Virtual Environment**:
    * For conda:
    ```bash
    conda create -n myenv python=3.12.3
    conda activate myenv
    ```

4. **Install Dependencies**:
    With your Conda environment activated, install the required Python packages specified in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application 🏃
**Note:** Make sure that the virtual environment remains activated while running the application.

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

3. **Run the Streamlit App**:
    Open **another** terminal window and navigate to the directory where the Streamlit app is located:
    ```bash
    cd HomeAssignmentML/App
    ```

This will open the Streamlit interface in your default web browser at `http://localhost:8501`.
