mjpg_streamer -o "output_http.so -w ./www -p 8080" -i "input_raspicam.so -x 1280 -y 720 -fps 30 -rot 180" -i "input_uvc.so -d /dev/video0 -r 1280x720 -f 30"
