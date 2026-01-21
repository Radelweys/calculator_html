import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder upload
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("the_file")

        if not file or file.filename == "":
            return "Tidak ada file"

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        return f"File {filename} berhasil diupload"

    return render_template("upload.html")