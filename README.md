# Text Clustering Application for Patent Analysis

## Introduction
This application is designed to analyze and group patent claims into topics, enhancing understanding of the mobile communications sector. It leverages advanced text processing techniques to dynamically cluster patent texts based on user input regarding the desired number of groups. The backend is built with FastAPI and integrates with a Streamlit frontend for a user-friendly interactive experience.

## Getting Started

### Prerequisites
To run this application, you'll need Python installed on your machine. The application was developed using Python 3.8, and compatibility with other versions is not guaranteed.

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
    conda create -n myenv 
    conda activate myenv

    * Other option:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. **Install Dependencies**:
    With your Conda environment activated, install the required Python packages specified in `requirements.txt`:
    ```bash
    pip install -r requirements.txt

