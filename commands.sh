# Install necessary python packages for running Flask app.
make install

az webapp up -n boston-housing-prediction-flask --sku F1
