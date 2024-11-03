# MyServer

This is a Python server for the product recommendation project. It uses Django to handle requests and responses. The code for modal is on some other repo, here we are using the pre built modal.pkl file for predications. 

## Setup

1. Clone the repository *:
    ```bash
    git clone https://github.com/Sami3160/product-recommendation-django-server.git

    cd /myserver
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages *:
    ```bash
    pip install django djangorestframework scikit-learn joblib pandas
    ```

## Running the Server

To run the server, use the following command:
```bash
python manage.py runserver
```

## Loading Scaler and Model Objects

Make sure to update the paths while loading the scaler and model objects in your code. For example:
```python
import joblib

scaler = joblib.load('/path/to/your/scaler.pkl')
model = joblib.load('/path/to/your/model.pkl')
```

Replace `/path/to/your/scaler.pkl` and `/path/to/your/model.pkl` with the actual paths to your scaler and model files.

## Testing
Using the Server with Postman
Open Postman and create a new GET request.

Set the URL to:
```
http://127.0.0.1:8000/api/recommend
```
Set the request body to raw and select Raw format. Use the following JSON structure:
```
{
    "product_data": [
        {
            "product_id": 123,
            "product_name": "Santoor",
            "view_time": 2,
            "visit_count": 3,
            "liked": 1
        },
        {
            "product_id": 124,
            "product_name": "iphone 11",
            "view_time": 90,
            "visit_count": 11,
            "liked": 1
        },
        {
            "product_id": 125,
            "product_name": "blue shirt",
            "view_time": 5,
            "visit_count": 1,
            "liked": 0
        },
        {
            "product_id": 126,
            "product_name": "laptop",
            "view_time": 30,
            "visit_count": 20,
            "liked": 0
        }
    ]
}
```
The response will also be in json with highest recommended product on top.
## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License.