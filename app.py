import os

import cv2
from dotenv import load_dotenv
from flask import Flask, Response, render_template

load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
DEBUG = bool(os.environ.get("DEBUG"))

RTMP_URL = os.environ.get("RTMP_URL")

app = Flask(__name__)
app.debug = DEBUG
app.active_video = False


@app.route("/")
@app.route("/clock")
def clock():
    """Display the current time"""
    app.active_video = False
    return render_template("pages/clock.html")


@app.route("/rtmp")
def rtmp():
    app.active_video = True
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
