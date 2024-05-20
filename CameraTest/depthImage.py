########################################################################
#
# Copyright (c) 2022, STEREOLABS.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################

import pyzed.sl as sl
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def main():
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD1080 # Use HD720 opr HD1200 video mode, depending on camera type.
    init_params.camera_fps = 30  # Set fps at 30
    init_params.depth_mode = sl.DEPTH_MODE.ULTRA # Set the depth mode to performance (fastest)
    init_params.coordinate_units = sl.UNIT.MILLIMETER  # Use millimeter units


    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Camera Open : "+repr(err)+". Exit program.")
        exit()


    # Capture 50 frames and stop
    i = 0
    image = sl.Mat()
    depth = sl.Mat()
    point_cloud = sl.Mat()
    normal_map = sl.Mat()
    runtime_parameters = sl.RuntimeParameters()
    while i < 1:
        # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # A new image is available if grab() returns SUCCESS
            zed.retrieve_image(image, sl.VIEW.LEFT)
            zed.retrieve_image(depth, sl.VIEW.DEPTH) # Retrieve depth matrix. Depth is aligned on the left RGB image
            zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA) # Retrieve colored point cloud
            zed.retrieve_measure(normal_map,sl.MEASURE.NORMALS)
            npimage=normal_map.get_data()
            cv.imshow('BGR_image',npimage)
            cv.waitKey(0)
            timestamp = zed.get_timestamp(sl.TIME_REFERENCE.CURRENT)  # Get the timestamp at the time the image was captured
            print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(image.get_width(), image.get_height(),
                  timestamp.get_milliseconds()))
            i = i + 1
            

    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()