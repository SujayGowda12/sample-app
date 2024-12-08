from flask import Flask, request, render_template
import logging

sample = Flask(__name__)

logging.basicConfig(
    filename='/home/ec2-user/sample-app/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Flask application has started")

@sample.route("/")
def main():
    logging.info("Main endpoint accessed")
    return render_template("index.html")

if __name__ == "__main__":
    logging.info("Starting Flask application on port 5000")
    sample.run(host="0.0.0.0", port=5000)

