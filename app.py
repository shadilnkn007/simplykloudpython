import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    storage_account = os.getenv("STORAGE_ACCOUNT_NAME")
    container = os.getenv("CONTAINER_NAME")
    blob_name = os.getenv("BLOB_NAME")
    sas_token = os.getenv("SAS_TOKEN")

    background_url = None

    if all([storage_account, container, blob_name, sas_token]):
        background_url = (
            f"https://{storage_account}.blob.core.windows.net/"
            f"{container}/{blob_name}{sas_token}"
        )

    return render_template(
        "index.html",
        background_url=background_url
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
