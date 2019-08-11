# Motion-Detection

Motion detector will observe the difference between consecutive frames. When the difference is high, it can be assume that motion was found. 
In order to prevent false positives, we will observe the standard deviation of the frame. 
When motion of a suitably sized object is detected, the standard deviation will rise, allowing us to trigger a motion event.[[1]](https://software.intel.com/en-us/node/754940)

Our program will be laid out as follows:

    Import OpenCV and its dependencies
    Initialize values
    Start video loop
        Calculate distance between frames.
        Shift frames
        Apply Gaussian blur to distance mapping
        Apply thresholding
        Calculate standard deviation
    If motion detected is above threshold, then print a message.
    Show the video.
