# CSV_Manager
A Django web application that allows users to upload CSV files and search through the uploaded data efficiently.

# MyProject

MyProject is a Django-based web application that allows users to upload CSV files and perform searches on the uploaded data. This project provides an easy way to manage and search through data imported from CSV files.

## Features

- **File Upload:** Users can upload CSV files through a web interface.
- **Data Search:** Users can search for specific entries in the uploaded CSV data.
- **Admin Interface:** The application includes an admin interface for managing the uploaded data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12.1
- Django 5.0.4
- SQLite (default database)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/BEXXISSAM/CSV_Manager
    cd CSV_Manager
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### Uploading a CSV File

1. Navigate to the upload page at `http://127.0.0.1:8000/upload`.
2. Select a CSV file from your computer.
3. Click the "Upload" button to upload the file.

### Searching Data

1. Navigate to the search page at `http://127.0.0.1:8000/search`.
2. Enter the search term in the search box.
3. Click the "Search" button to view the results.

## Project Structure

- `myproject/`: Project root directory.
- `SIWebSite/`: Django app containing the core functionality.
- `Files/`: Directory where uploaded files are stored.
- `media/`: Directory for storing media files.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django management script.

## Models

### ImportFileModel

This model represents the uploaded CSV files.

- `date`: Date and time of the upload.
- `file`: FileField to store the uploaded CSV file.
- `activated`: Boolean field to indicate if the file is processed.

### RIDModel

This model represents the data imported from the CSV files.

- `Jour`: DateField for the date.
- `Prefecture`: CharField for the prefecture.
- `csc`: CharField for the CSC.
- `TYPE`: CharField for the type.
- `RID_ID`: CharField for the RID ID.
- `STATUT_paquet`: CharField for the status.
- `Commentaire`: TextField for comments.

## Contributing

To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please feel free to contact us at [issamxoz@gmail.com](mailto:issamxoz@gmail.com).

