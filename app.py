import os

import cv2
from dotenv import load_dotenv
from flask import Flask, Response, render_template, request

load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
DEBUG = bool(os.environ.get("DEBUG"))

RTMP_URL = os.environ.get("RTMP_URL")

app = Flask(__name__)
app.debug = DEBUG
app.active_video = False


@app.after_request
def video_feed_check(response):
    """Toggle stream reading based on URL."""
    if "/static" not in request.url:
        if request.url.endswith("rtmp"):
            app.active_video = True
        else:
            app.active_video = False
    return response


@app.route("/")
@app.route("/clock")
def clock():
    """Display the current time."""
    return render_template("pages/clock.html")


@app.route("/rtmp")
def rtmp():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


def gen_frames():
    url = RTMP_URL
    camera = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
    while app.active_video:
        # gmt = time.gmtime(time.time())
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            # if gmt.tm_sec % 1 == 0:
            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
            )  # concat frame one by one and show result


@app.route("/video-feed")
def video_feed():
    """Render video stream"""
    return render_template("/pages/video_feed.html")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
