import os
import subprocess

path_input = "./input"

resolution_list = ['1920×1080', '1280×720', '720×480', '640×480',
                   '512×384', '382×288', '320×240']
crf_list = [18, 19, 20, 22, 25, 27, 30, 35, 40, 45, 50, 55]

for subdirs, dirs, files in os.walk(path_input):
    for file in files:
        os.makedirs("output/" + str(file).split(".")[0])
        for resolution in resolution_list:
            for crf in crf_list:
                media_in = subdirs + "/"+ file
                media_out = "./output/" + str(file).split(".")[0] + '/compressed_' + str(resolution) + "_crf_" + str(crf) + "_" + file
                subprocess.run("ffmpeg -i " + media_in.replace(" ", "\\ ") + " -y -vcodec libx264 -filter:v scale=w=" +
                               str(resolution.split("×")[0]) + ":h=" + str(resolution.split("×")[1]) +
                               " -crf " + str(crf) + " " + media_out.replace(" ", "\\ "), shell=True)
