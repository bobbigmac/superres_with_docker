# Docker image

Install [docker_python-opencv-ffmpeg](https://github.com/Borda/docker_python-opencv-ffmpeg), then run as below.

See [Deep Learning based Super Resolution with OpenCV](https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066)

# Run

```
docker run -v /home/bobbigmac/projects/a_demos/opencv/:/test/ --rm -it python-opencv-ffmpeg:py36 python /test/test-upsize.py
docker run -v G:\\projects\\opencv:/test/ --rm -it python-opencv-ffmpeg:py36 python /test/test-upsize.py
```

# Models

There are currently 4 different SR models supported in the module. They can all upscale images by a scale of 2, 3 and 4. LapSRN can even upscale by a factor of 8. They differ in accuracy, size and speed.

- EDSR [1]. This is the best performing model. However, it is also the biggest model and therefor has the biggest file size and slowest inference. You can download it here.
- ESPCN [2]. This is a small model with fast and good inference. It can do real-time video upscaling (depending on image size). You can download it here.
- FSRCNN [3]. This is also small model with fast and accurate inference. Can also do real-time video upscaling. You can download it here.
- LapSRN [4]. This is a medium sized model that can upscale by a factor as high as 8. You can download it here.

# TODO

- Need imput parameters and multiple model switching