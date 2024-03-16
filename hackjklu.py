

from roboflow import Roboflow
rf = Roboflow(api_key="ySpCrhE9fr6O1ApQKiUj")
project = rf.workspace("viren-dhanwani").project("tennis-ball-detection")
version = project.version(6)
dataset = version.download("yolov8")

